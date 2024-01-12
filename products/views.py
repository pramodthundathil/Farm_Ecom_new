from django.shortcuts import render, redirect
from .forms import Productaddform
from  .models import Product, Blog, Cart, Purchase, Reviews
from django.contrib import messages
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

razorpay_client = razorpay.Client(
  auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

# Create your views here.

def MyProducts(request):
    form = Productaddform
    products = Product.objects.filter(user = request.user)
    if request.method == "POST":
        form = Productaddform(request.POST,request.FILES)
        if form.is_valid():
            prod = form.save()
            prod.user = request.user
            prod.save()
            messages.info(request,"Product added to list")
            return redirect('MyProducts')
    context = {
        "form":form,
        "products":products
    }
    return render(request, "myproducts.html",context)

def Blogs(request):
    blogs =  Blog.objects.all()
    context = {
        "blogs":blogs
    }
    return render(request,'blog.html',context)

def About(request):
    return render(request,"about.html")

def CartPage(request):
    cart = Cart.objects.filter(user = request.user)
    total = 0
    for i in cart:
        total = total + i.TotalPrice
    
    context = {
        "cart":cart,
        "total":total,
        'items':len(cart)
    }
    return render(request,'cart.html',context)
    
@login_required(login_url="SignIn")
def AddToCart(request,pk):
    product = Product.objects.get(id = pk)
    cart = Cart.objects.create(user = request.user, product = product,Quantity = 1,TotalPrice = product.Product_price)
    cart.save()
    return redirect("CartPage")

def CartRemove(request,pk):
    Cart.objects.get(id = pk).delete()
    messages.info(request,"item deleted")
    return redirect("CartPage")

def CartIncresse(request,pk):
    cart = Cart.objects.get(id = pk)
    cart.Quantity = cart.Quantity + 1
    cart.save()
    cart.TotalPrice = cart.product.Product_price * cart.Quantity
    cart.save()
    return redirect("CartPage")

def CartDecrease(request,pk):
    cart = Cart.objects.get(id = pk)
    if cart.Quantity == 1:
        cart.delete()
    else:
        cart.Quantity = cart.Quantity - 1
        cart.save()
        cart.TotalPrice = cart.product.Product_price * cart.Quantity
        cart.save()
    return redirect("CartPage")

def Checkout(request,total):
    cart = Cart.objects.filter(user = request.user)
    for i in cart:
        purchase = Purchase.objects.create(user = request.user, product = i.product,Quantity = i.Quantity,TotalPrice = i.TotalPrice,status = "Item ordered")
        purchase.save()
        i.delete()
    currency = 'INR'
    amount = float(total) * 100 # Rs. 200
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                          currency=currency,
                          payment_capture='0'))
    

  # Create a Razorpay Order Pyament Integration.....
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                          currency=currency,
                          payment_capture='0'))

  # order id of newly created order.
    razorpay_order_id = razorpay_order["id"]
    callback_url = 'paymenthandlercus'

  # we need to pass these details to frontend.
    context = {}
    context = {"total":total}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url 
    context['slotid'] = "1",
    # context['amt'] = (product1.Product_price)*float(qty)

    return render(request,"payment.html",context)


@csrf_exempt
def paymenthandlercus(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

      # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result is not None:
                amount = 800 * 100 # Rs. 200
                try:
                    print("working 1")
                    razorpay_client.payment.capture(payment_id, amount)
                    return redirect('Index')
          # render success page on successful caputre of payment
                except:
                    print("working 2")
                    return redirect('Index')
                    
                    
          # if there is an error while capturing payment.
            else:
                return render(request, 'Index')
        # if signature verification fails.    
        except:
            return HttpResponseBadRequest()
        
      # if we don't find the required parameters in POST data
    else:
  # if other than POST request is made.
        return HttpResponseBadRequest()

def PurchaseHistory(request):
    context = {
        "purchase":Purchase.objects.filter(user=request.user)
    }
    return render(request, "purchasehistory.html",context)

def AllProducts(request):
    product = Product.objects.all()
    return render(request,"allproducts.html",{"product":product})

def BlogSingle(request,pk):
    blog = Blog.objects.get(id=pk)
    return render(request, "blogsingle.html",{"blog":blog})

def DeleteProduct(request,pk):
    Product.objects.get(id = pk).delete()
    messages.info(request,"Prodduct deleted....")
    return redirect("MyProducts")

def Search(request):
    if request.method == "POST":
        ser = request.POST['search']
        context = {
            "location":Product.objects.filter(Product_Location__contains = ser ),
            "name": Product.objects.filter(Product_Name__contains = ser) 
        }
        return render(request, "searchres.html",context)

def OrderStatus(request):
    purchase = Purchase.objects.filter(product__user = request.user)
    context = {
        "purchase":purchase
    }
    return render(request,"customerorders.html",context)

def OrderstatusChange(request,pk,str):

    if str == "accept":
        purchase = Purchase.objects.get(id = pk)
        purchase.status = "Order Accepted"
        purchase.save()
        messages.info(request,"Order status Changed")
        return redirect("OrderStatus")

    elif str == "despatch":
        purchase = Purchase.objects.get(id = pk)
        purchase.status = "Order despatched"
        purchase.save()
        messages.info(request,"Order status Changed")
        return redirect("OrderStatus")
    elif str == "delivered":
        purchase = Purchase.objects.get(id = pk)
        purchase.status = "Order delivered"
        purchase.save()
        messages.info(request,"Order status Changed")
        return redirect("OrderStatus")
    elif str == "cancel":
        purchase = Purchase.objects.get(id = pk)
        purchase.status = "Order Cancelled"
        purchase.save()
        messages.info(request,"Order status Changed")
        return redirect("OrderStatus")
    elif str == "delete":
        purchase = Purchase.objects.get(id = pk).delete()
        messages.info(request,"Item Deleted")
        return redirect("OrderStatus")

    return redirect("OrderStatus")

def ViewProduct(request,pk):
    product = Product.objects.get(id = pk)
    reviews = Reviews.objects.filter(product = product)
    context = {
        "product":product,
        "reviews":reviews
    }
    return render(request,"productsigngleview.html",context)


def ReviewAdd(request,pk):
    if request.method == "POST":
        product = Product.objects.get(id = pk)
        review = request.POST["review"]
        re = Reviews.objects.create(product = product, reviewer = request.user,review = review)
        re.save()
        messages.info(request,"Review Added..")

    return redirect("ViewProduct", pk =pk)