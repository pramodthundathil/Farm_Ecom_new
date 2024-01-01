from django.urls import path
from .import views

urlpatterns = [
    path("MyProducts",views.MyProducts,name="MyProducts"),
    path("Blogs",views.Blogs,name="Blogs"),
    path("About",views.About,name="About"),
    path("CartPage",views.CartPage,name="CartPage"),
    path("AddToCart/<int:pk>",views.AddToCart,name="AddToCart"),
    
    
    
  
]