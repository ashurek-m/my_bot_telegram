import telebot
from telebot import types
import constant
import exped
import pandas as pd
import support

bot = telebot.TeleBot(constant.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, support.instruction)



@bot.message_handler(content_types=['text'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button_1 = types.InlineKeyboardButton(text="Нажми меня", callback_data="test")
    callback_button_2 = types.InlineKeyboardButton(text="no", callback_data="test")
    keyboard.add(callback_button_1, callback_button_2)
    bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)
def text_s(message):
    bot.send_message(message.chat.id, 'я прототип')
    bot.register_next_step_handler(message, text_m)
def text_m(message):
    bot.send_message(message.chat.id, 'я учусь')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Пыщь!")
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")

bot.polling(none_stop=True, interval=5)