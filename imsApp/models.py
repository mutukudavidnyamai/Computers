from re import I
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from more_itertools import quantify
from django.db.models import Sum

# Create your models here.


    
# Create your models here. 
class Employee(models.Model):
    address = models.EmailField(max_length=100,null=True)
    first_name = models.CharField(max_length=50,null=True)
    sec_name = models.CharField(max_length=50,null=True)       
    department = models.CharField(max_length= 50,null=True)
    company = models.CharField(max_length= 50,null=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' - ' + self.department
    
class Product(models.Model):
    model=models.CharField(max_length=50, null=True)
    serial=models.CharField(max_length=50, null=True)
    hd_size=models.CharField(max_length=50,null=True)
    ram=models.CharField(max_length=50, null=True)
    processor=models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=2, choices=(('1','Assigned'),('2','Unassigned')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serial + ' - ' + self.model

    def count_inventory(self):
        stocks = Stock.objects.filter(product = self)
        stockIn = 0
        stockOut = 0
        for stock in stocks:
            if stock.type == '1':
                stockIn = int(stockIn) + int(stock.quantity)
            else:
                stockOut = int(stockOut) + int(stock.quantity)
        available  = stockIn - stockOut
        return available

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    type = models.CharField(max_length=2,choices=(('1','Stock-in'),('2','Stock-Out')), default = 1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.serial + ' - ' + self.product.model

class Category(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=2, choices=(('1','Active'),('2','Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name