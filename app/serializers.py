from pyexpat import model
from rest_framework import serializers
from app.models import product_list, product, market, category, sub_category, brand
""" serializers """


class SuperMarketSerializer(serializers.ModelSerializer):
    """class SuperMarkets serializer"""
    class Meta:
        """class Meta"""
        model = market
        fields = ('Name', 'url')


class product_listSerializer(serializers.ModelSerializer):
    """class product_list Serializer"""
    class Meta:
        """class Meta"""
        model = product
        fields = ('id', 'name', 'img_url',
                  'brand_id', 'cat_id', 'sub_id')


class productSerializer(serializers.ModelSerializer):
    """class product serializer"""
    class Meta:
        """class Meta"""
        model = product_list
        fields = ('product_id', 'price', 'product_url',
                  'market_id', 'update_date')

class categorySerializer(serializers.ModelSerializer):
    """class category serializer"""
    class Meta:
        model = category
        fields = ('name')

class sub_categorySerializer(serializers.ModelSerializer):
    """ class sub-category serializer """
    class Meta:
        model = sub_category
        fields = ('name', 'cat_id')

class brandSerializer(serializers.ModelSerializer):
    """ class brand serializer """
    class Meta:
        model = brand
        fields = ('name')
