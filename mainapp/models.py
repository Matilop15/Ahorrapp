from django.db import models

# class Providers(models.Model):
#     provider_name = models.CharField(max_length=30)
#     provider_website = models.URLField(blank=True, null=True)


class Product(models.Model):
    product_name = models.CharField(max_length=80, blank=True, null=True)
    brand_name = models.CharField(max_length=30, blank=True, null=True)
    # provider_id = models.ForeignKey(Providers, related_name='product',on_delete=models.CASCADE)
    provider_name = models.CharField(max_length=30)
    product_price = models.CharField(max_length=10, blank=True, null=True)
    img_url = models.URLField(blank=True, null=True)
    product_url = models.URLField(blank=True)
    update_date = models.DateTimeField()

