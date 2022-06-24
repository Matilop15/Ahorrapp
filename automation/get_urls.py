import requests

#change parameter dependiendo de que supermercado quiera buscar

#anterior forma de hacerlo

#for prod_id in range(4, 188, 4):
 #   prod = requests.get("https://www.ahorrapp.me/api/products/{}"
  #             .format(prod_id))
   # name = prod.json()
    #products = dict(product_url=name['product_url'])
    #print(products)
    #for key, value in products.items():
     #   if key[1]:
      #      print( "\"" + value + "\",")

#new forma

urls = {
    "1": "https://www.ahorrapp.me/api/disco-products/",
    "2": "https://www.ahorrapp.me/api/geant-products",
    "3": "https://www.ahorrapp.me/api/tata-products/",
    "4": "https://www.ahorrapp.me/api/tienda-inglesa-products/"
}
for i in urls.values():
    each_url = i
    prod = requests.get(each_url)
    name = prod.json()
    for i in name:
        for key, value in i.items():
            if key == 'product_url':
                print( "\"" + value + "\",")
