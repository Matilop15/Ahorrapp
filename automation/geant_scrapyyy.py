from asyncio.base_subprocess import WriteSubprocessPipeProto
from urllib import response
from bs4 import BeautifulSoup
import requests

api = "https://www.ahorrapp.me/api/geant-products/"

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
            price = soup.find('label', class_='skuBestInstallmentValue').get_text()
            price = price[2:]
            if price[2] == ",":
                price = price[:3]
            elif price[3] == ",":
                price = price[:4]
            print(id_prod)