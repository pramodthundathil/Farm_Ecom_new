from django.urls import path
from .import views

urlpatterns = [
    path("MyProducts",views.MyProducts,name="MyProducts")
]