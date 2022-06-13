import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from racacmc import raca_price
from fm import fm_price
from bstscmc import bsts_price
from buffcmc import buffdoge_price
from dd import dd_price

telegram_bot_token = "2086965891:AAHRiYskD36ZIZ7SSUkjC_0nDxOUKYpD_LE"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

#price list
bsts = bsts_price
fm = fm_price
raca = raca_price
buffdoge = buffdoge_price
dd = dd_price

def cuan(update, context):
    chat_id = update.effective_chat.id
    message = f"Salam Profit. \U0001F911"
    print('Succesfully Send')
    context.bot.send_message(chat_id=chat_id, text=message)

def memek(update, context):
    chat_id = update.effective_chat.id
    message = f"Yametkudasi \U0001F921"
    print('Succesfully Send')
    context.bot.send_message(chat_id=chat_id, text=message)
    
def binjai(update, context):
    chat_id = update.effective_chat.id
    message = f"Salam dari Binjai \U0001F64F"
    print('Succesfully Send')
    context.bot.send_message(chat_id=chat_id, text=message) 
    
    
def kontol(update, context):
    chat_id = update.effective_chat.id
    message = f"SAYA BURN KOIN TAPI KOK KOIN SAYA ILANG 50JT."
    print('Succesfully Send')
    context.bot.send_message(chat_id=chat_id, text=message)    
     
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
dispatcher.add_handler(CommandHandler("cuan", cuan))
dispatcher.add_handler(CommandHandler("memek", memek))
dispatcher.add_handler(CommandHandler("binjai", binjai))
dispatcher.add_handler(CommandHandler("kontol", kontol))
dispatcher.add_handler(CommandHandler("bsts", bsts))
dispatcher.add_handler(CommandHandler("watchlist", watchlist))
dispatcher.add_handler(CommandHandler("dd", dd))

updater.start_polling()