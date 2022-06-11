from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand
from django.utils import timezone
from mainapp.models import Product


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the product data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from data.csv into our product table"

    def handle(self, *args, **options):
        if  Product.objects.exists():
            print('Product data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        
        print("Loading product data from csv into product table")
        for row in DictReader(open('./data.csv')):
            product = Product()
            product.product_name = row['Title']
            product.product_price = row['Price']
            product.product_url = row['Title_URL']
            product.img_url = row['Image']
            product.brand_name = row['Brand']
            product.update_date = timezone.now()
            product.save()
