from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://api.pancakeswap.info/api/v2/tokens/0xb2c31b08e393a3e3f6aed9db8c5bd503fde3fa72'
session = Session()
response = session.get(url)
data = json.loads(response.text)['data']['price']


float_data = "DD $" + "%.16f" % float(data)
dd_price = float_data 
print(dd_price)

