import os
import requests
from flask import Flask, request
import re
import time
import telebot
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from telebot import types
import random


TOKEN = "1071595338:AAFAPoo4xsxgAHd-HuQC5NmjnAadlwmrkLI"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

user_dict = {}
class User:
    def __init__(self, header):
        self.header = header
        self.pic = pic
        
@bot.message_handler(commands=['start'])
def test(m):
  bot.send_message(m.chat.id,text="akhill")
        
@bot.message_handler(func=lambda message:True, content_types=['photo'])
def command_default(m):
  photo_id = m.photo[-1].file_id
  tt = m.caption
  User.pic = photo_id
  bot.send_message(m.chat.id,text="send now pdisk Title")
  kya="\n"
  tag_split = tt.splitlines()
  for each_cn in tag_split:
    new_cn = each_cn.strip()
    kya+=f"<code>{new_cn}</code>"
  m = bot.send_message(m.chat.id,text=kya,parse_mode="html")
  bot.register_next_step_handler(m, channel1)


def channel1(m):
  User.header = m.text
  m = bot.send_message(m.chat.id,text="send now pdisk Link")
  bot.register_next_step_handler(m, channel2)
  
def channel2(m):
  photo1 = f"{User.pic}"
  head = f"{User.header}"
  link = m.text
  myre = '^(http|https)://'
  t1 = f"🔞 {head}"
  t2 = "\n━━━━━━━━━━━━━━━━━━━━"
  t3 = f"\n📥 Download now\n{link}\n\n✅ Watch online \n◼️ <a href='{link}'>480p</a> 🔶 <a href='{link}'>720p</a> ◼️"
  t4= "\n━━━━━━━━━━━━━━━━━━━━"
  t5 = "\nWATCH ONLINE OR DOWNLOAD\n(Just Install PLAYit App from playstore)\n🚀 Fastest Speed || 🔆 No Buffering"
  caption1 = f"<b>{t1}{t2}{t3}{t4}{t5}</b>"
  if re.search(myre,f"{link}"):
    bot.send_photo(chat_id="-1001246111561",photo=f'{photo1}',caption=f"{caption1}",parse_mode="html")
    bot.send_message(m.chat.id,text="posted")
  else:
    m = bot.send_message(m.chat.id,text="link is not valid send again pdisk Link")
    bot.register_next_step_handler(m, channel2)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://couple13.herokuapp.com/' + "1071595338:AAFAPoo4xsxgAHd-HuQC5NmjnAadlwmrkLI")
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))