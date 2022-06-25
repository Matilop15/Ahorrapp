from asyncio.base_subprocess import WriteSubprocessPipeProto
from urllib import response
from bs4 import BeautifulSoup
import requests

api = "https://www.ahorrapp.me/api/geant-products/"

respuesta = requests.get(api)
responses = respuesta.json()
for i in responses:
    for key, value in i.items():
        geant_prices = {}
        if key == 'id':
            id_prod = value
        if key == 'product_url' and value != "-":
            website = value
            respons = requests.get(website)
            if respons.status_code == 200:
                contents = respons.text
                soup = BeautifulSoup(contents, 'lxml')
                price = soup.find('label', class_='skuBestInstallmentValue').get_text()
                price = price[3:]
                for i in range(len(price)):
                    if price[i] == ',':
                        price = price[:i]
                        break
                geant_prices[id_prod] = price
                print(geant_prices)