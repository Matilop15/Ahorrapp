from django.contrib import admin
from .models import ProductMarket, Product, SuperMarket
"""admin panel"""
# Register your models here.

admin.site.register(SuperMarket)
admin.site.register(Product)
admin.site.register(ProductMarket)
