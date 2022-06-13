from django.contrib import admin
from .models import Product, Supermarket  # added this
# Register your models here.

admin.site.register(Product) # added this
admin.site.register(Supermarket)

""" Django provides us with an admin interface out of the box; the interface will make it easy to test CRUD operations on the Recipe model we just created, but first, we will do a little configuration. """
