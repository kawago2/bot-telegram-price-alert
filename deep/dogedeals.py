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
driver.get("https://poocoin.app/tokens/0xb2c31b08e393a3e3f6aed9db8c5bd503fde3fa72")
x_path = '//*[@id="root"]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/span'

def price_dd():
    price_dd_element = driver.find_element(By.XPATH,x_path)
    price_dd = price_dd_element.text
    return price_dd

if __name__ == "__main__":
    print(price_dd())