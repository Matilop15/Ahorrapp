from rest_framework import serializers
from .models import Product, Supermarket
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "product", "super_market_id", "product_price", "description", "url", "updated_at")

class SupermarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermarket
        fields = ("id", "address", "phone", "url", "map")
