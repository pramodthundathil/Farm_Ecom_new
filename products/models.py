from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    options = (
    ("Fruits","Fruits"),
    ("Vegetable","Vegetable"),
    ("fertilizers","fertilizers"),
    ("other","other")
    )
    
    Product_Name = models.CharField(max_length=244)
    Product_Category = models.CharField(max_length=255,choices=options)
    Product_price = models.IntegerField()
    Product_Discription = models.CharField(max_length=1000)
    Product_Stock = models.IntegerField(null=True,blank=True)
    Product_Image = models.FileField(upload_to="Customer_products")
    Product_Location = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    