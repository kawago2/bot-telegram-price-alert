import requests
import json

link = 'https://api.pancakeswap.info/api/v2/tokens/0xc77dd3ade7b717583e0924466e4e474a5673332c'
r = requests.get(link)
data = r.json()

def price_bsts():
    name = data['data']['symbol']
    price = data['data']['price']
    price_bsts = f"{name} {price}"
    return price_bsts

if __name__ == "__main__":
    print(price_bsts())