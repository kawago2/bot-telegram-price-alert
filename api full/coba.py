import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from racacmc import raca_price
from fm import fm_price
from bstscmc import bsts_price
from buffcmc import buffdoge_price
from dd import dd_price

telegram_bot_token = "" # TOKEN BOT TELEGRAM

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

#price list
bsts = bsts_price
fm = fm_price
raca = raca_price
buffdoge = buffdoge_price
dd = dd_price

    
def bsts(update, context):
    chat_id = update.effective_chat.id  
    bsts = bsts_price
    message = f"{bsts}"
    print('Succesfully Send')
    context.bot.send_message(chat_id=chat_id, text=message)
 

def facemeta(update, context):
    chat_id = update.effective_chat.id
    fm = fm_price
    message = f"{fm}"
    print('Succesfully Send')
    context.bot.send_message(chat_id=chat_id, text=message)
    
def raca(update, context):
    chat_id = update.effective_chat.id
    raca = raca_price
    message = f"{raca}"
    print('Succesfully Send')
    context.bot.send_message(chat_id=chat_id, text=message)
    
def buffdoge(update, context):
    chat_id = update.effective_chat.id
    buffdoge = buffdoge_price
    message = f"{buffdoge}"
    print('Succesfully Send')
    context.bot.send_message(chat_id=chat_id, text=message)
    
def dd(update, context):
    chat_id = update.effective_chat.id
    dd = dd_price
    message = f"{dd}"
    print('Succesfully Send')
    context.bot.send_message(chat_id=chat_id, text=message)
    
    
def watchlist(update, context):
    chat_id = update.effective_chat.id
    fm = fm_price
    raca = raca_price
    bsts = bsts_price
    dd = dd_price
    buffdoge = buffdoge_price
    message = f"watchlist\n{bsts}\n{raca}\n{buffdoge}\n{dd}\n{fm}"
    print('Succesfully Send')
    context.bot.send_message(chat_id=chat_id, text=message)
    

    
dispatcher.add_handler(CommandHandler("buffdoge", buffdoge))    
dispatcher.add_handler(CommandHandler("facemeta", facemeta))
dispatcher.add_handler(CommandHandler("raca", raca))
dispatcher.add_handler(CommandHandler("bsts", bsts))
dispatcher.add_handler(CommandHandler("watchlist", watchlist))
dispatcher.add_handler(CommandHandler("dd", dd))

updater.start_polling()