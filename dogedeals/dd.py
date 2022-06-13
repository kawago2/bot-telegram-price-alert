from selenium import webdriver # to install type pip install selenium in commandline
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium.webdriver.common.by import By
import time 
import datetime
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import telegram_send # pip install telegram-send
    
driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome('/chromedriver.exe',options=option)
driver.get("https://poocoin.app/tokens/0xb2c31b08e393a3e3f6aed9db8c5bd503fde3fa72")

def price():
    price = driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/span").text
    current_time = str(datetime.datetime.now())
    telegram_send.send(messages=["Doge Deals " + price])
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