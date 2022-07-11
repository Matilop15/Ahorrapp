from django.core.management import BaseCommand
from django.utils import timezone
from bs4 import BeautifulSoup
from app.models import product
import requests


class Command(BaseCommand):
    """ This command handles Tienda product urls to scrap updated prices"""
    def handle(self, *args, **options):
        headers = requests.utils.default_headers()
        headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0', })
        prod_request = "https://www.ahorrapp.me/api/tienda-inglesa-products/"
        prods = requests.get(prod_request).json()
        for prod in prods:
            for key, value in prod.items():
                if key == 'product_url' and value != "-":
                    prod_url = value
                    resp = requests.get(prod_url, headers=headers)
                    if resp.status_code == 200:
                        content = resp.text
                        soup = BeautifulSoup(content, 'lxml')
                        if soup.find('script', type="application/ld+json").get_text():
                            box = soup.find('script', type="application/ld+json").get_text()
                            box = eval(box)
                            for key, value in box.items():
                                if key == "offers":
                                    for key, val in value.items():
                                        if key == 'price':
                                            for i in range(len(val)):
                                                if val[i] == ".":
                                                    new_price = val[:i]
                                                    break
                            product.objects.filter(product_url=prod_url).update(price=new_price, update_date=timezone.now())
                            print(f"{prod_url} --- > Price updated")
                        else:
                            print(f"{prod_url} ---> Price not found")
                    else:
                        print(f"{prod_url} ---> Page not found, price update skipped")
