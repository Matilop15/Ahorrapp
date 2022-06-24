from urllib import request, response
from mechanize import Browser
from bs4 import BeautifulSoup
import requests


headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

api = "https://www.ahorrapp.me/api/tienda-inglesa-products/"

respuesta = requests.get(api)
responses = respuesta.json()
for i in responses:
    for key, value in i.items():
        disco_prices = {}
        if key == 'id':
            id_prod = value
        if key == 'product_url' and value != "-":
            website = value
            respons = requests.get(website, headers=headers)
            contents = respons.text
            soup = BeautifulSoup(contents, 'lxml')
            box = soup.find('script', type="application/ld+json").get_text()
            box = eval(box)
            for key, value in box.items():
                if key == "offers":
                    for key, new_price in value.items():
                        if key == 'price':
                            if new_price[2] == ".":
                                new_price = new_price[:2]
                            elif new_price[3] == ".":
                                new_price = new_price[:3]
                            disco_prices[id_prod] = new_price
                            print(disco_prices)

