import telebot
import os
import requests
from flask import Flask, request
import re
import telebot
from telebot import types
import random
from translate 
import Translator
from langdetect 
import detect

TOKEN = "1221370836:AAGzjvpt18Dvw2vw5hsbxE0fQS6q_1_NveY"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)


user_dict = {}
class User:
    def __init__(self, header):
        self.header = header
        self.pic = pic

@bot.message_handler(commands=['test']) # welcome message handler
def send_welcome(m):
    chat_id = m.chat.id
    if chat_id in id_a:
        bot.send_message(chat_id, '☺️ Bot is running (VIP USER)')
    else:
        bot.send_message(chat_id, '☺️ Bot is running (FREE USER)')
        #bot.send_message(m.chat.id, text="☺️ Bot is running")

id_a = [818396979 ,608824855]



 



@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://shayarib.herokuapp.com/' + "1221370836:AAGzjvpt18Dvw2vw5hsbxE0fQS6q_1_NveY")
    return "!", 200



if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
