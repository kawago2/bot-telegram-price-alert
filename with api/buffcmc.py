from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':'DOGECOIN',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '',  # API KEYS
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
data = json.loads(response.text)['data']['DOGECOIN']['quote']['USD']['price']
float_data = "BuffDoge " + "%.16f" % float(data)
buffdoge_price = float_data 
print(buffdoge_price)
