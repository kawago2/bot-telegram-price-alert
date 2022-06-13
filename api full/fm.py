from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://api.pancakeswap.info/api/v2/tokens/0x3e0b5807515756635c6347cdeebf95946e604bcf'
session = Session()
response = session.get(url)
data = json.loads(response.text)['data']['price']

float_data = "FACEMETA $" + "%.16f" % float(data)
fm_price = float_data 
print(fm_price)

