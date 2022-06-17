from rest_framework import serializers
from app.models import SuperMarket, Product, ProductMarket


class SuperMarketSerializer(serializers.ModelSerializer):
    """class SuperMarketsSerializer"""
    class Meta:
        """class Meta"""
        model = SuperMarket
        fields = ('SuperMarketId', 'Address', 'Name', 'Phone')


class ProductSerializer(serializers.ModelSerializer):
    """class ProductSerializer"""
    class Meta:
        """class Meta"""
        model = Product
        fields = ('ProductId', 'UrlImg', 'Brand')


class ProductMarketSerializer(serializers.ModelSerializer):
    """ProductMarketSerializer class"""
    class Meta:
        """class Meta"""
        model = ProductMarket
<<<<<<< HEAD
        fields = ('ProductMarketId', 'SuperMarketId', 'ProductId', 'UpdateAt', 'ProductPrice')
=======
        fields = ('ProductMarketId', 'SuperMarketId', 'ProductId',
                'ProductName', 'ProductPrice')
                
>>>>>>> 557daebebd98278cf0bfe29c7ed66bcd201f377f
