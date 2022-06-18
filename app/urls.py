from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import ProductMarketViewSet, ProductViewSet, SuperMarketViewSet
""" defines URLs """

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'supermarkets', SuperMarketViewSet)
router.register(r'productmarkets', ProductMarketViewSet)
# router.register(r'products-supermarket', AllProductsViewSet)

urlpatterns = [
    path("", include(router.urls))
]
