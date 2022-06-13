import requests
import json

link = 'https://api.pancakeswap.info/api/v2/tokens/0x23125108bc4c63E4677b2E253Fa498cCb4B3298b'
r = requests.get(link)
data = r.json()

def price_buff():
    name = data['data']['symbol']
    price = data['data']['price']
    price_buff = f"{name} {price}"
    return price_buff

if __name__ == "__main__":
    print(price_buff())