import telebot
import constant

bot = telebot.TeleBot(constant.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я готов выполнять задание')



bot.polling(none_stop=True, interval=0)