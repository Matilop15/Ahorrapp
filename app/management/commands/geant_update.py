from django.core.management import BaseCommand
from django.utils import timezone
from bs4 import BeautifulSoup
from app.models import product
import requests


class Command(BaseCommand):
    """ This command handles Geant product urls to scrap updated prices"""
    def handle(self, *args, **options):
        prod_request = "https://www.ahorrapp.me/api/geant-products/"
        prods = requests.get(prod_request).json()
        for prod in prods:
            for key, value in prod.items():
                if key == 'product_url' and value != "-":
                    prod_url = value
                    resp = requests.get(prod_url)
                    if resp.status_code == 200:
                        content = resp.text
                        soup = BeautifulSoup(content, 'lxml')
                        if soup.find('label', class_='skuBestInstallmentValue').get_text()[3:]:
                            new_price = soup.find('label', class_='skuBestInstallmentValue').get_text()[3:]
                            for i in range(len(new_price)):
                                if new_price[i] == ',':
                                    new_price = new_price[:i]
                                    break
                            product.objects.filter(product_url=prod_url).update(price=new_price, update_date=timezone.now())
                            print(f"{prod_url} --- > Price updated")
                        else:
                            print(f"{prod_url} ---> Price not found")
                    else:
                        print(f"{prod_url} ---> Page not found, price update skipped")
