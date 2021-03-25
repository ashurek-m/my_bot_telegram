import telebot
import constant

bot = telebot.TeleBot(constant.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')



bot.polling(none_stop=True, interval=0)