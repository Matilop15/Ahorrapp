from django.contrib import admin
from .models import SuperMarket, Product, ProductMarket

# Register your models here.
admin.site.register(SuperMarket)
admin.site.register(Product)
admin.site.register(ProductMarket)
