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
def item_message(message):
    bot.send_message(message.chat.id, 'введите итем')
    bot.register_next_step_handler(message, 'item' + lock_item)

@bot.message_handler(commands=['order'])
def order_message(message):
    bot.send_message(message.chat.id, 'введите номер интересующего вас заказа')
    bot.register_next_step_handler(message, 'order' + lock_item)

@bot.message_handler(content_types=['text'])
def lock_item(message):
    if 'item' in message.text:
        try:
            df = exped.df_exped
            item = int(message.text)
            bot.send_message(message.chat.id, exped.item_filter(item, df))
        except KeyError:
            bot.send_message(message.chat.id, 'такого итема нет в базе')
        except ValueError:
            bot.send_message(message.chat.id, 'введите номер итема цыфрами')
    elif 'order' in message.text:
        try:
            df = exped.df_exped
            order = int(message.text)
            bot.send_message(message.chat.id, exped.text_filter_by_order(order, df))
        except KeyError:
            bot.send_message(message.chat.id, 'такого заказа нет в базе')
            bot.register_next_step_handler(message, lock_order)
        except ValueError:
            bot.send_message(message.chat.id, 'введите номер заказа цыфрами')


bot.polling(none_stop=True, interval=0)