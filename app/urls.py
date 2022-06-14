from django.urls import re_path
from app import views


urlpatterns = [
    re_path(r'^product$', views.product_api),
    re_path(r'^product/([0-9]+)$', views.product_api)
]
