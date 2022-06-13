import requests
import json


link = 'https://api.pancakeswap.info/api/v2/tokens/0x12bb890508c125661e03b09ec06e404bc9289040'
r = requests.get(link)
data = r.json()

def price_raca():
    name = data['data']['symbol']
    price = data['data']['price']
    price_raca = f"{name} {price}"
    return price_raca

if __name__ == "__main__":
    print(price_raca())