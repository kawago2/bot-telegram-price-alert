import requests
from selenium import webdriver # to install type pip install selenium in commandline
from selenium.webdriver.common.by import By
import datetime
import time 

driver = webdriver.Chrome()
driver.get("https://poocoin.app/tokens/0x23125108bc4c63e4677b2e253fa498ccb4b3298b")


def price_buffdoge():
    price_buffdoge = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/span").text
    print(price_buffdoge)
    return price_buffdoge

if __name__ == "__main__":
    print(price_buffdoge())