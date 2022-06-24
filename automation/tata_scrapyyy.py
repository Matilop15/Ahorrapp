from urllib import response
from bs4 import BeautifulSoup
import requests



api = "https://www.ahorrapp.me/api/tata-products/"

respuesta = requests.get(api)
responses = respuesta.json()
for i in responses:
    for key, value in i.items():
        tata_prices = {}
        if key == 'id':
            id_prod = value
        if key == 'product_url'  and value != "-":
            website = value
            respons = requests.get(website)
            contents = respons.text
            soup = BeautifulSoup(contents, 'lxml')
            box = soup.find('em', class_='valor-dividido')
            price = box.find('strong').get_text()
            price = price[2:]
            for i in range(len(price)):
                if price[i] == ",":
                    price = price[:i]
                    break
            tata_prices[id_prod] = price
            print(tata_prices)