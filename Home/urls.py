from django.urls import path
from .import views

urlpatterns = [
    path("",views.Index,name="Index"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("Userprofile",views.Userprofile,name="Userprofile"),
    path("OrderUserprofile/<int:pk>",views.OrderUserprofile,name="OrderUserprofile"),


    
]
