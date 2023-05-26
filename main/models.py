from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/category/')


    def __str__(self):
        return self.category
    
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/products/')
    price =  models.IntegerField()
    discount= models.IntegerField(null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Info(models.Model):
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.email
    
class Main(models.Model):
    title1 = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/main/')

    def __str__(self):
        return str(self.id)
    
class Shop(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE,related_name='shop_client')
    date =models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    def __str__(self):
        return str(self.client)
    

class ShopItems(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE,related_name='item_savatcha')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='item_product')
    quantity = models.IntegerField()
    totalPay = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)


class Contacting(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200 , null=True,blank=True)
    text = models.TextField()

    def __str__(self):
        return self.name
class Bloging(models.Model):
    title = models.CharField(max_length=200)
    name =  models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/blog/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    text = models.TextField()
    
    def __str__(self):
        return self.title

