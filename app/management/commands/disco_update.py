from bs4 import BeautifulSoup
import requests
from app.models import product
from django.core.management import BaseCommand
from django.utils import timezone

class Command(BaseCommand):

    def handle(self, *args, **options):
        api = "https://www.ahorrapp.me/api/disco-products/"
        respuesta = requests.get(api)
        responses = respuesta.json()
        for i in responses:
            for key, value in i.items():
                prod_url = value
                if key == 'product_url' and value != "-":
                    website = value
                    respons = requests.get(website)
                    contents = respons.text
                    soup = BeautifulSoup(contents, 'lxml')
                    box = soup.find('div', itemtype='http://schema.org/Offer')
                    price = box.findAll('meta')[1]
                    prices = str(price)
                    new_price = prices[15:18]
                    for i in range(len(new_price)):
                        if new_price[i] == ".":
                            new_price = new_price[:i]
                            break
                    print(new_price)
                    product.objects.filter(product_url=prod_url).update(price=new_price, update_date=timezone.now())
