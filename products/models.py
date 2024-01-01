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
    
    def __str__(self):
        return self.Product_Name 
    

class Blog(models.Model):
    options = (
    ("Fruits","Fruits"),
    ("Vegetable","Vegetable"),
    ("fertilizers","fertilizers"),
    ("other","other")
    )
    
    Blog_name = models.CharField(max_length = 255)
    Blog_category = models.CharField(max_length = 255,choices = options)
    Blog_Discription = models.CharField(max_length = 1000)
    Disease = models.CharField(max_length = 255)
    Disease_Discription = models.CharField(max_length = 1000)
    Symptoms = models.CharField(max_length = 255)
    Symptoms_Discription = models.CharField(max_length = 1000)
    Remedy = models.CharField(max_length = 1000)
    Other = models.CharField(max_length = 1000)
    Blog_image = models.FileField(upload_to="blogs")
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    Quantity = models.FloatField()
    TotalPrice = models.FloatField()
    
class Purchase(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    Quantity = models.FloatField()
    TotalPrice = models.FloatField()
    date = models.DateField(auto_now_add = True)
    status = models.CharField(max_length=255)
    
    
    