from django.shortcuts import render
from .forms import Productaddform
from  .models import Product
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
            return redirect('ProductAdd')
    context = {
        "form":form,
        "products":products
    }
    return render(request, "myproducts.html",context)
