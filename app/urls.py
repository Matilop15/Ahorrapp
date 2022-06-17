from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductMarketViewSet, ProductViewSet, SuperMarketViewSet
""" defines URLs """

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'supermarkets', SuperMarketViewSet)
router.register(r'productmarkets', ProductMarketViewSet)

urlpatterns = [
<<<<<<< HEAD
    path("", include(router.urls))
=======
    re_path(r'^api/product/', views.product_api),
    re_path(r'^api/product/([0-9]+)$', views.product_api),
    re_path(r'^api/productmarket/$', views.product_market_api),
    re_path(r'^api/productmarket/([0-9]+)$', views.product_market_api),
    re_path(r'^api/supermarket/$', views.super_markets_api),
    re_path(r'^api/supermarket/([0-9]+)$', views.super_markets_api),
>>>>>>> 557daebebd98278cf0bfe29c7ed66bcd201f377f
]
