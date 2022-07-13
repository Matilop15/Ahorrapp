import json
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
                    headers = requests.utils.default_headers()
                    headers.update({"cookie": "_gid=GA1.3.889241208.1656630112; VTEXSC=sc=4; ISSMB=ScreenMedia=0&UserAcceptMobile=False; SGTS=7C6596D8574F8B0665E5887D94CAC3C0; nvg73700=95d1b225736f50e072e112e3a09|2_182; VtexRCSessionIdv7=bfe2e992-a297-45b9-b55d-5bf139d60113; checkout.vtex.com=__ofid=59af8bd0ca0e467688600c9a709b8d6c; .ASPXAUTH=DB772FB45BB831E7552C2513C543EB516D81E8C7320D94C1E9547E1806ECAA6A54713E5F27131CE324DD19F25E7961A6FF42FDE0E7CAFADF216D0FA2249F1F14D8F465AEC7D672AA07F25640972F3911B2FCFABCFB7CB086489C3ED76F3A47DE50AB3EDA767464541FCF159B8EFBA29CFE562E5FFD386F8E2C750ABAD00842210D556AC2A1A2E588742C841E4E381A8F98B214AEE436636E501FB631AB60937B53039F39; _gcl_au=1.1.297734044.1656630180; VtexRCMacIdv7=2a55cd8b-1e51-4025-8764-d061273dd832; vtex_session=eyJhbGciOiJFUzI1NiIsImtpZCI6IjRGQzJDMDcyOTBFNkQ1NThGNjNCMDJBRTVBQ0U3MzkwMzVDMzdDRTQiLCJ0eXAiOiJqd3QifQ.eyJhY2NvdW50LmlkIjoiM2YwOGEyODEtYTVkNC00NjlmLWFmNGUtYmZiMWZhMDgxNTc2IiwiaWQiOiJlNzRjMDM5YS0xMDkyLTQ1YjMtYThhYy03ZWRiMjQ1NjY5YjUiLCJ2ZXJzaW9uIjo1LCJzdWIiOiJzZXNzaW9uIiwiYWNjb3VudCI6InNlc3Npb24iLCJleHAiOjE2NTczMjE4MzYsImlhdCI6MTY1NjYzMDYzNiwiaXNzIjoidG9rZW4tZW1pdHRlciIsImp0aSI6ImE4M2JhZWE1LTA3NTgtNDgzNi1iYTRhLWI0ZmJhYjdlMTU5YyJ9.GLH5urNcdcQVNMdsuIRJIqX8cCbifm9Ou-V8AFOdPv5f4ynXAQ-X6O31lJMEAO6Hg6JGB-5YrwSIOYMsnE3eoA; vtex_segment=eyJjYW1wYWlnbnMiOm51bGwsImNoYW5uZWwiOiI0IiwicHJpY2VUYWJsZXMiOm51bGwsInJlZ2lvbklkIjoiVTFjamRHRjBZWFY1Ylc5dWRHVjJhV1JsYnc9PSIsInV0bV9jYW1wYWlnbiI6bnVsbCwidXRtX3NvdXJjZSI6bnVsbCwidXRtaV9jYW1wYWlnbiI6bnVsbCwiY3VycmVuY3lDb2RlIjoiVVlVIiwiY3VycmVuY3lTeW1ib2wiOiIkIiwiY291bnRyeUNvZGUiOiJVUlkiLCJjdWx0dXJlSW5mbyI6ImVzLVVZIiwiY2hhbm5lbFByaXZhY3kiOiJwdWJsaWMifQ; store-id=318; janus_sid=cc7e7967-47de-4bf2-955e-8fb40b1fb103; _ga_QNGFZT5SZJ=GS1.1.1656630139.1.1.1656632839.60; _ga=GA1.1.1485140311.1649118403"})
                    resp = requests.get(prod_url, headers=headers)
                    if resp.status_code == 200:
                        content = resp.text
                        soup = BeautifulSoup(content, 'lxml')
                        if soup.find('link', rel='canonical'):
                            box = soup.find('link', rel='canonical')
                            new_price = box.find_next('script').get_text()
                            new_price = new_price[16:]
                            new_price = new_price[:-100]
                            new_price = json.loads(new_price)
                            for key, value in new_price.items():
                                if key == "skus":
                                    value = value[-1]
                                    for key, val in value.items():
                                        if key == "fullSellingPrice":
                                            new_price = val
                                            new_price = new_price[2:]
                                            for i in range(len(new_price)):
                                                if new_price[i] == ",":
                                                    new_price = new_price[:i]
                                                    break
                            try:
                                new_price = int(new_price)
                            except ValueError:
                                print(f"{prod_url} --- > Out of stock")
                                break
                            product.objects.filter(product_url=prod_url).update(price=new_price, update_date=timezone.now())
                            print(f"{prod_url}--> {new_price} --- > Price updated")
                        else:
                            print(f"{prod_url} ---> Price not found")
                    else:
                        print(f"{prod_url} ---> Page not found, price update skipped")
