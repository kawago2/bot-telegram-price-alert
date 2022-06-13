import requests
from selenium import webdriver # to install type pip install selenium in commandline
from selenium.webdriver.common.by import By
import datetime
import time 

driver = webdriver.Chrome()
driver.get("https://poocoin.app/tokens/0xc77dd3ade7b717583e0924466e4e474a5673332c")


def price_bsts():
    price_bsts = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/span").text
    print(price_bsts)
    return price_bsts

if __name__ == "__main__":
    print(price_bsts())