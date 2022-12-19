from django.db import models

from datetime import datetime
from django.db import models 
import datetime

# Create your models here.
 
class registration(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=255, null=True)
    mobile = models.BigIntegerField()
    gender = models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.first_name



class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    images = models.ImageField(upload_to='upload/category/')


    def __str__(self):
        return self.name

class Product(models.Model):
    pro_name = models.CharField(max_length=200, null=True)
    price = models.IntegerField()
    desc = models.TextField(max_length=500, null=True)
    pro_image = models.ImageField(upload_to='upload/product/')
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.pro_name


class Order_dtls(models.Model):
    address = models.CharField(max_length=300,null=True)
    mobile = models.BigIntegerField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    customer = models.ForeignKey(registration, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    # date = models.DateTimeField(default=datetime.datetime.now())
    date = models.DateTimeField(auto_now_add = True)


def __str__(self):
    return self.customer.first_name


   