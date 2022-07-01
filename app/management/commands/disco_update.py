from django.core.management import BaseCommand
from django.utils import timezone
from bs4 import BeautifulSoup
from app.models import product
import requests


class Command(BaseCommand):
    """ This command handles Disco product urls to scrap updated prices"""
    def handle(self, *args, **options):
        prod_request = "https://www.ahorrapp.me/api/disco-products/"
        prods = requests.get(prod_request).json()
        for prod in prods:
            for key, value in prod.items():
                if key == 'product_url' and value != "-":
                    prod_url = value
                    response = requests.get(prod_url)
                    if response.status_code == 200:
                        contents = response.text
                        soup = BeautifulSoup(contents, 'lxml')
                        if soup.find('div', itemtype='http://schema.org/Offer'):
                            box = soup.find('div', itemtype='http://schema.org/Offer')
                            price = str(box.findAll('meta')[1])
                            new_price = price[15:18]
                            for i in range(len(new_price)):
                                if new_price[i] == ".":
                                    new_price = new_price[:i]
                                    break
                            product.objects.filter(product_url=prod_url).update(price=new_price, update_date=timezone.now())
                            print(f"{prod_url} --- > Price updated")
                        else:
                            print(f"{prod_url} ---> Price not found")
                    else:
                        print(f"{prod_url} ---> Page not found, price update skipped")
