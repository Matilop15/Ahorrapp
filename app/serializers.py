from rest_framework import serializers
from app.models import ProductMarket, SuperMarket, Product
""" serializers """


class SuperMarketSerializer(serializers.ModelSerializer):
    """class SuperMarketsSerializer"""
    class Meta:
        """class Meta"""
        model = SuperMarket
        fields = ('SuperMarketId', 'Address', 'Name', 'Phone')


class product_listSerializer(serializers.ModelSerializer):
    """class product_list Serializer"""
    class Meta:
        """class Meta"""
        model = Product
        fields = ('ProductId', 'UrlImg', 'Brand', 'Slug', 'Name')


class productSerializer(serializers.ModelSerializer):
    """class product serializer"""
    class Meta:
        """class Meta"""
        model = ProductMarket
        fields = ('ProductMarketId', 'SuperMarketId',
                  'ProductId', 'UpdateAt', 'ProductPrice')
