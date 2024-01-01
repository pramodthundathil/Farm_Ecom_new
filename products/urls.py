from django.urls import path
from .import views

urlpatterns = [
    path("MyProducts",views.MyProducts,name="MyProducts"),
    path("Blogs",views.Blogs,name="Blogs"),
    path("About",views.About,name="About"),
    path("CartPage",views.CartPage,name="CartPage"),
    path("AddToCart/<int:pk>",views.AddToCart,name="AddToCart"),
    path("CartRemove/<int:pk>",views.CartRemove,name="CartRemove"),
    path("CartIncresse/<int:pk>",views.CartIncresse,name="CartIncresse"),
    path("CartDecrease/<int:pk>",views.CartDecrease,name="CartDecrease"),
    path("Checkout/<str:total>",views.Checkout,name="Checkout"),
    path("paymenthandlercus",views.paymenthandlercus,name="/Checkout/paymenthandlercus"),
    path("PurchaseHistory",views.PurchaseHistory,name="PurchaseHistory"),
    path("AllProducts",views.AllProducts,name="AllProducts"),
    path("BlogSingle/<int:pk>",views.BlogSingle,name="BlogSingle"),
    path("DeleteProduct/<int:pk>",views.DeleteProduct,name="DeleteProduct"),
    path("Search",views.Search,name="Search"),


    
]