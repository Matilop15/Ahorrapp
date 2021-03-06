from rest_framework import viewsets
from rest_framework import generics
from django.http import JsonResponse
from .serializers import productSerializer, product_listSerializer, marketSerializer, market_productsSerializer
from .models import product, product_list, market
""" Defines views """


class productViewSet(viewsets.ReadOnlyModelViewSet):
    """ product view Set """
    serializer_class = productSerializer
    queryset = product.objects.all()


class marketViewSet(viewsets.ReadOnlyModelViewSet):
    """ market view Set """
    serializer_class = marketSerializer
    queryset = market.objects.all()


class product_listViewSet(viewsets.ReadOnlyModelViewSet):
    """ product list view set """
    serializer_class = product_listSerializer
    queryset = product_list.objects.all()


class disco_productsViewSet(viewsets.ReadOnlyModelViewSet):
    """ disco market products view Set """
    serializer_class = market_productsSerializer
    queryset = product.objects.all().filter(market_id=1)


class geant_productsViewSet(viewsets.ReadOnlyModelViewSet):
    """ geant market products view set """
    serializer_class = market_productsSerializer
    queryset = product.objects.all().filter(market_id=2)


class tata_productsViewSet(viewsets.ReadOnlyModelViewSet):
    """ tata market products view set """
    serializer_class = market_productsSerializer
    queryset = product.objects.all().filter(market_id=3)


class tiendainglesa_productsViewSet(viewsets.ReadOnlyModelViewSet):
    """ tienda inglesa market products view set """
    serializer_class = market_productsSerializer
    queryset = product.objects.all().filter(market_id=4)
