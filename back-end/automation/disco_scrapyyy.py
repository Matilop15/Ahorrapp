from ast import Index
from urllib import response
from bs4 import BeautifulSoup
import requests

api = "https://www.ahorrapp.me/api/disco-products/"

respuesta = requests.get(api)
responses = respuesta.json()
for i in responses:
    for key, value in i.items():
        disco_prices = {}
        if key == 'id':
            id_prod = value
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
            disco_prices[id_prod] = new_price
            print(disco_prices)
