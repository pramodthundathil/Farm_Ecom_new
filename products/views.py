from django.shortcuts import render, redirect
from .forms import Productaddform
from  .models import Product, Blog, Cart, Purchase
from django.contrib import messages


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
    
    context = {
        "cart":cart
    }
    return render(request,'cart.html',context)

def AddToCart(request,pk):
    product = Product.objects.get(id = pk)
    cart = Cart.objects.create(user = request.user, product = product,Quantity = 1,TotalPrice = product.Product_price)
    cart.save()
    return redirect("CartPage")