from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SupermarketViewSet
"""
In the code above, the router class generates the following URL patterns:
    . /recipes/ - CREATE and READ operations can be performed on this route.
    . /recipes/{id} - READ, UPDATE, and DELETE operations can be performed on this route.
"""

router = DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'supermarket', SupermarketViewSet)

urlpatterns = [
    path("", include(router.urls))
]
