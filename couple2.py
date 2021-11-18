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
from datetime import datetime
from datetime import date 
import pytz
from datetime import timedelta
from random import sample
from config import Config


TOKEN = Config.BOT_TOKEN
#TOKEN = "1902307802:AAG0D1WZSDVCzWWsMzwSAXJq_1-O9MDsNA4"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

ist1 = pytz.timezone('Asia/Calcutta')
currentTimeIST = datetime.now(ist1)

authid = []

@bot.message_handler(commands=['start'])
def test(m):
  ak = bot.send_message(m.chat.id,text=f"{authid}")
  bot.register_next_step_handler(ak,admnyflmvid)

@bot.message_handler(commands=['check'])
def test(m):
  ak = bot.send_message(m.chat.id,text=f"{authid}")

def admnyflmvid(m):
  authid.clear()
  authid.append(m.text)
  
@bot.message_handler(commands=['python'])
def akhil(m):
  while True:
    ist1 = pytz.timezone('Asia/Calcutta')
    CurrentTime=datetime.now(ist1)
    minute1 = int(CurrentTime.strftime("%M"))
    #seconds1 = int(CurrentTime.strftime("%S"))
    if int(minute1)%19 == 0:
      r = requests.get("https://akhilmeen.herokuapp.com/")
      bot.send_message(m.chat.id,text= f"{r.status_code}")
      time.sleep(60)
    else:
      continue
  
  
  
  
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