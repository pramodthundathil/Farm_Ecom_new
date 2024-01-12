from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import UserAddForm
from django.contrib.auth.models import User
from products.models import Product
from .models import UserData


# Create your views here.

def Index(request):
    products = Product.objects.all()
    context = {
        "product":products
    }
    return render(request,"index.html",context)


def SignIn(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pswd']
        user1 = authenticate(request, username = username , password = password)
        
        if user1 is not None:
            
            request.session['username'] = username
            request.session['password'] = password
            login(request, user1)
            return redirect('Index')
        
        else:
            messages.info(request,'Username or Password Incorrect')
            return redirect('SignIn')
    return render(request,"login.html")

def SignUp(request):
    form = UserAddForm()
    if request.method == "POST":
        form = UserAddForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Exists")
                return redirect('SignUp')
            if User.objects.filter(email = email).exists():
                messages.info(request,"Email Exists")
                return redirect('SignUp')
            else:
                new_user = form.save()
                new_user.save()
                
                # group = Group.objects.get(name='user')
                # new_user.groups.add(group) 
                
                messages.success(request,"User Created")
                return redirect('SignIn')
            
    return render(request,"register.html",{"form":form})



def SignOut(request):
    logout(request)
    return redirect('Index')


def Userprofile(request):
    if UserData.objects.filter(user = request.user).exists():
        user = UserData.objects.get(user = request.user)
    else:
        user = UserData.objects.create(
            name = "Nil",
            house = "Nil",
            phone = "nil",
            city = "nil",
            state = "nil",
            user = request.user
        )
        user.save()
        return redirect("Userprofile")

    if request.method == "POST":
        user.phone = request.POST["phone"]
        user.house = request.POST["house"]
        user.city = request.POST["city"]
        user.state = request.POST["state"]
        user.save()

    context = {
        "user":user
    }
    return render(request,"userprofile.html",context)

def OrderUserprofile(request,pk):
    userid = User.objects.get(id = pk)
    user = UserData.objects.get(user = userid)

    context = {'user':user}

    return render(request,"orderprofile.html",context)
