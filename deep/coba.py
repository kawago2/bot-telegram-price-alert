import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

telegram_bot_token = "2086965891:AAHRiYskD36ZIZ7SSUkjC_0nDxOUKYpD_LE"

updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher


def cuan(update, context):
    chat_id = update.effective_chat.id
    message = f"Salam Profit. \U0001F911"
    context.bot.send_message(chat_id=chat_id, text=message)
    
def binjai(update, context):
    chat_id = update.effective_chat.id
    message = f"Salam dari Binjai \U0001F64F"
    context.bot.send_message(chat_id=chat_id, text=message) 
    
    
def kontol(update, context):
    chat_id = update.effective_chat.id
    message = f"SAYA BURN KOIN TAPI KOK KOIN SAYA ILANG 50JT."
    context.bot.send_message(chat_id=chat_id, text=message)    
     
def bsts(update, context):
    chat_id = update.effective_chat.id  
    message = f"/price"
    context.bot.send_message(chat_id=chat_id, text=message)
 

def facemeta(update, context):
    chat_id = update.effective_chat.id
    message = f"/price"
    context.bot.send_message(chat_id=chat_id, text=message)
    
def dd(update, context):
    chat_id = update.effective_chat.id
    message = f"/price@Poocoin_Pricebot 0xb2c31b08e393a3e3f6aed9db8c5bd503fde3fa72"
    context.bot.send_message(chat_id=chat_id, text=message)
    
def raca(update, context):
    chat_id = update.effective_chat.id
    message = f"/price"
    context.bot.send_message(chat_id=chat_id, text=message)
    
def buffdoge(update, context):
    chat_id = update.effective_chat.id
    message = f"/price"
    context.bot.send_message(chat_id=chat_id, text=message)
    
    
dispatcher.add_handler(CommandHandler("facemeta", facemeta))
dispatcher.add_handler(CommandHandler("dd", dd))
dispatcher.add_handler(CommandHandler("raca", raca))
dispatcher.add_handler(CommandHandler("buffdoge", buffdoge))
dispatcher.add_handler(CommandHandler("cuan", cuan))
dispatcher.add_handler(CommandHandler("binjai", binjai))
dispatcher.add_handler(CommandHandler("kontol", kontol))
dispatcher.add_handler(CommandHandler("bsts", bsts))
updater.start_polling()