from rest_framework import serializers
from app.models import SuperMarkets, Product, ProductMarket


class SuperMarketsSerializer(serializers.ModelSerializer):
    """class SuperMarketsSerializer"""
    class Meta:
        """class Meta"""
        model = SuperMarkets
        fields = ('SuperMarketId', 'Address', 'Url', 'Phone')

class ProductSerializer(serializers.ModelSerializer):
    """class ProductSerializer"""
    class Meta:
        """class Meta"""
        model = Product
        fields = ('ProductId', 'Name', 'UrlImg', 'Brand')

class ProductMarketSerializer(serializers.ModelSerializer):
    """ProductMarketSerializer class"""
    class Meta:
        """class Meta"""
        model = ProductMarket
        fields = ('ProductMarketId', 'SuperMarketId', 'ProductId', 'ProductName', 'ProductPrice')