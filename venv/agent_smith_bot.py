import telebot
import constant
import exped
import pandas as pd

bot = telebot.TeleBot(constant.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я готов выполнять задание')

@bot.message_handler(content_types=['text'])
def lock_item(message):
    df = exped.df_exped
    item = int(message.text)
    bot.send_message(message.chat.id, exped.item_filter(item, df))

bot.polling(none_stop=True, interval=0)