# -*- coding: utf-8 -*-
import telebot
import constants

bot = telebot.TeleBot(constants.token)

    
bot.message_handler(content_types=["text"])


def handle_text(message):
    if message.text == "а":
        bot.send_message(message.chat.id, "б")
    elif message.text == "б":
        bot.send_message(message.chat.id, "г")
    else:
        bot.send_message(message.chat.id, "не понял")


bot.polling(none_stop=True, interval=0)
