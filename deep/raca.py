import requests
from selenium import webdriver # to install type pip install selenium in commandline
from selenium.webdriver.common.by import By
import datetime
import time 

driver = webdriver.Chrome()
driver.get("https://poocoin.app/tokens/0x12bb890508c125661e03b09ec06e404bc9289040")


def price_raca():
    price_raca = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/span").text
    print(price_raca)
    return price_raca

if __name__ == "__main__":
    print(price_raca())