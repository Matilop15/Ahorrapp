from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'brand_name', 'provider_name', 'product_price', 'img_url', 'product_url', 'update_date']
