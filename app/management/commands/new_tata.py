from django.core.management import BaseCommand
from django.utils import timezone
from bs4 import BeautifulSoup
from app.models import product
import requests



class Command(BaseCommand):
    """ This command handles Tata product urls to scrap updated prices"""
    def handle(self, *args, **options):
        prod_request = "https://www.ahorrapp.me/api/tata-products/"
        prods = requests.get(prod_request).json()
        for prod in prods:
            for key, value in prod.items():
                if key == 'product_url' and value != "-":
                    prod_url = value
                    prod_url = value + "?storeId=318"
                    resp = requests.get(prod_url)
                    if resp.status_code == 200:
                        content = resp.text
                        soup = BeautifulSoup(content, 'lxml')
                        first_call = soup.find('link', rel='canonical')
                        first_json = first_call.find_next('script')
                        first_json = first_json.text
                        jsoon = first_json.split('"productId":')[1]
                        id_prod = jsoon.split(',"name"')[0]
                        headers = requests.utils.default_headers()
                        headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'})
                        second_call = requests.get("https://www.tata.com.uy/api/catalog_system/pub/products/search?fq=productId:" + id_prod + "&sc=4", headers=headers)
                        json_two = second_call.text
                        print(json_two)
                        content = json_two.split('{"Value":')[1]
                        new_price = content.split(',"InterestRate"')[0]
                        for i in range(len(new_price)):
                            if new_price[i] == "," or new_price[i] == ".":
                                new_price = new_price[:i]
                                break
                        print(new_price)
                        product.objects.filter(product_url=prod_url).update(price=new_price, update_date=timezone.now())
                        print(f"{prod_url} --- > Price updated")
                    else:
                        print(f"{prod_url} ---> Page not found, price update skipped")
