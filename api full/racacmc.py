from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'symbol':'RACA',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'b3e82654-6a30-4180-8553-4f1dbc6b3bd3',
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
data = json.loads(response.text)['data']['RACA']['quote']['USD']['price']
float_data = "RACA $" + "%.16f" % float(data)
raca_price = float_data 
print(raca_price)
