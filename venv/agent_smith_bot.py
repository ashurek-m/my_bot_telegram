import telebot
import constant
import exped
import pandas as pd

bot = telebot.TeleBot(constant.token)
df = exped.df_exped
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я готов выполнять задание')

@bot.message_handler(content_types=['text'])
def lock_item(message):
    item = message
    answer = exped.item_filter(item, df)
    bot.send_message(message.chat.id, 'df.info()')

bot.polling(none_stop=True, interval=0)