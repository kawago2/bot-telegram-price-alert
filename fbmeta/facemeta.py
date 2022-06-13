from selenium import webdriver # to install type pip install selenium in commandline
from selenium.webdriver.common.by import By
import time 
import datetime
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import telegram_send # pip install telegram-send
    
driver = webdriver.Chrome()
driver.get("https://poocoin.app/tokens/0x3e0b5807515756635c6347cdeebf95946e604bcf")

def price():
    price = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/span").text
    current_time = str(datetime.datetime.now())
    telegram_send.send(messages=["FACEMETA " + price])
    print(price)
    time.sleep(120)
   # telegram
    
while True:
    try:
        time.sleep(1)
        price()
    except Exception as e:
        driver.quit
        break