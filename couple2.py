import os
import requests
from flask import Flask, request
import re
import time
import telebot
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import time
import random, string
import telebot
from telebot import types
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
from random import sample
from config import Config


TOKEN = Config.BOT_TOKEN
#TOKEN = "1902307802:AAG0D1WZSDVCzWWsMzwSAXJq_1-O9MDsNA4"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

authid = [818396979]

@bot.message_handler(commands=['start'])
def test(m):
  bot.send_message(m.chat.id,text="akhill")

 
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
 
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://' + Config.app + '.herokuapp.com/' + f"{TOKEN}")
    return "!", 200
 
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
