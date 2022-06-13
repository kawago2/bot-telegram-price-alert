import requests
from selenium import webdriver # to install type pip install selenium in commandline
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from IPython.display import Image
import datetime
import time 
import json

driver = webdriver.Chrome()
driver.get("https://poocoin.app/tokens/0x3e0b5807515756635c6347cdeebf95946e604bcf")
x_path = '//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/span'


def price_facemeta():
    price_facemeta_element = driver.find_element(By.XPATH,x_path)
    price_facemeta = price_facemeta_element.text
    return price_facemeta

if __name__ == "__main__":
    print(price_facemeta())