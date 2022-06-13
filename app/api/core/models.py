from django.db import models

from django.db import models
# Create your models here.

class Supermarket(models.Model):
    """class Supermarket"""
    address = models.CharField(max_length=120)
    phone = models.IntegerField()
    url = models.CharField(max_length=120)
    map = models.CharField(max_length=120)

class Product(models.Model):
    """class Product"""
    product = models.CharField(max_length=120)
    product_price = models.IntegerField()
    img = models.FileField()
    description = models.CharField(max_length=400)
    super_market_id = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    updated_at = models.DateField()

    def __str_(self):
        return "Recipe for {}".format(self.name)
