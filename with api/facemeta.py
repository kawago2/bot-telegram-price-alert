import requests
import json


link = 'https://api.pancakeswap.info/api/v2/tokens/0x3e0b5807515756635c6347cdeebf95946e604bcf'
r = requests.get(link)
data = r.json()

def price_facemeta():
    name = data['data']['symbol']
    price = data['data']['price']
    price_facemeta = f"{name} {price}"
    return price_facemeta

if __name__ == "__main__":
    print(price_facemeta())