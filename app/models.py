from datetime import datetime
from django.db import models
""" module that defines database models """


class Product(models.Model):
    """class products model"""
    ProductId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=120)
    UrlImg = models.CharField(max_length=120)
    Brand = models.CharField(max_length=120)
    Slug = models.SlugField(max_length=120)


class SuperMarket(models.Model):
    """class SuperMarkets model"""
    SuperMarketId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=120)
    Address = models.CharField(max_length=120)
    Phone = models.CharField(max_length=120)


class ProductMarket(models.Model):
    """class ProductMarket"""
    ProductMarketId = models.AutoField(primary_key=True)
    SuperMarketId = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
    ProductId = models.ForeignKey(Product, on_delete=models.CASCADE)
    ProductPrice = models.CharField(max_length=45)
    UpdateAt = models.DateTimeField(auto_now=True)
