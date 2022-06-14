from django.db import models

# Create your models here.

class Product(models.Model):
    """class products model"""
    ProductId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=120)
    UrlImg = models.CharField(max_length=120)
    Brand = models.CharField(max_length=120)

class SuperMarkets(models.Model):
    """class SuperMarkets model"""
    SuperMarketId = models.AutoField(primary_key=True)
    Address = models.CharField(max_length=120)
    Url = models.CharField(max_length=120)
    Phone = models.IntegerField()

class ProductMarket(models.Model):
    """class ProductMarket"""
    ProductMarketId = models.AutoField(primary_key=True)
    SuperMarketId = models.ForeignKey(SuperMarkets, on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    ProductName = models.CharField(max_length=120)
    ProductPrice = models.IntegerField()
