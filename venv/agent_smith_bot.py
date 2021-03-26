import telebot
import constant
import exped
import pandas as pd
import support

bot = telebot.TeleBot(constant.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, support.instruction)

@bot.message_handler(commands=['item'])
def start_message(message):
    bot.send_message(message.chat.id, 'введите итем')
    bot.register_next_step_handler(message, lock_item)


@bot.message_handler(content_types=['text'])
def lock_item(message):
    try:
        df = exped.df_exped
        item = int(message.text)
        bot.send_message(message.chat.id, exped.item_filter(item, df))
    except KeyError:
        bot.send_message(message.chat.id, 'такого итема нет в базе')
    except ValueError:
        bot.send_message(message.chat.id, 'введите номер итема цифрами')


bot.polling(none_stop=True, interval=0)