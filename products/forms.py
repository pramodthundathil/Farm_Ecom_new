from django.forms import ModelForm 
from .models import Product

class Productaddform(ModelForm):
    class Meta:
        model = Product
        fields = ["Product_Name","Product_Category","Product_price","Product_Stock","Product_Location", "Product_Discription","Product_Image"]