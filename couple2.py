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
import config


#TOKEN = config.BOT_TOKEN
#TOKEN = "1902307802:AAG0D1WZSDVCzWWsMzwSAXJq_1-O9MDsNA4"
bot = telebot.TeleBot(token=config.BOT_TOKEN)
server = Flask(__name__)



scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credential.json", scope)
client = gspread.authorize(creds)
ak = client.open("pdiskv2")
sheet1 = ak.worksheet(config.SEETA)
 
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
  kya=""
  tag_split = tt.splitlines()
  for each_cn in tag_split:
    new_cn = each_cn.strip()
    myre = '^(http|https)://'
    if re.search(myre,f"{each_cn}"):
      kya+=f"\n{new_cn}"
    else:
      kya+=f"\n<code>{new_cn}</code>"
  myString = f"{tt}"
  #linkkksss = re.search("(?P<url>https?://[^\s]+)", myString).group("url")
  linkkksss = re.findall(r'(https?://\S+)', myString)
  m = bot.send_message(m.chat.id,text=f"{kya}\n\n\n\n{linkkksss}",parse_mode="html")
  bot.register_next_step_handler(m, channel1)
 
 
def channel1(m):
  User.header = m.text
  if m.text == "/start":
    bot.send_message(m.chat.id,text="send it again /start")
  else:
    m = bot.send_message(m.chat.id,text="send now pdisk Link")
    bot.register_next_step_handler(m, channel2)
  
def channel2(m):
  if m.text == "/start":
    bot.send_message(m.chat.id,text="send it again /start")
  else:
    photo1 = f"{User.pic}"
    head = f"{User.header}"
    link = m.text
    myre = '^(http|https)://'
    t1 = f"🔞 {head}"
    t2 = "\n━━━━━━━━━━━━━━━━━━━━"
    t3 = f"\n📥 Download now\n{link}\n✅ Watch online \n◼️ <a href='{link}'>480p</a> 🔶 <a href='{link}'>720p</a> ◼️"
    t4= "\n━━━━━━━━━━━━━━━━━━━━"
    t5 = "\nWATCH ONLINE OR DOWNLOAD\n(Just Install PLAYit App from playstore)\n🚀 Fastest Speed || 🔆 No Buffering"
    caption1 = f"<b>{t1}{t2}{t3}{t4}{t5}</b>"
    if re.search(myre,f"{link}"):
      values_list2 = sheet3.col_values(1)
      for i in values_list2:
        try:
          bot.send_photo(chat_id=f"{i}",photo=f'{photo1}',caption=f"{caption1}",parse_mode="html")
        except:
          bot.send_message(m.chat.id,text=f"{i} failed")
      chotu=bot.send_photo(chat_id="-1001551862526",photo=f'{photo1}',caption=f"{caption1}",parse_mode="html")
      akhil=chotu.message_id
      sheet3.update("D20",akhil)
      bot.send_message(m.chat.id,text=f"Done")
    else:
      m = bot.send_message(m.chat.id,text="link is not valid send again pdisk Link")
      bot.register_next_step_handler(m, channel2)
 
 
@bot.channel_post_handler(func=lambda message:True, content_types=['text'])
def chatid2(message):
  fnd = "✅ Watch online"
  ttt = message.text
  ak = fnd in ttt
  if f"{ak}" == "False":
    h = sheet1.get('D20').first()
    sequence = [i for i in range(int(h))]
    subset = sample(sequence, 3)
    for i in subset:
      pstid = random.randrange(2,int(h)-1)
      bot.forward_message(chat_id = message.chat.id, from_chat_id = "-1001551862526", message_id = f"{pstid}")
      time.sleep(2)
  else:
    print("np")
 
 
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200
 
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://' + config.app + '.herokuapp.com/' + config.BOT_TOKEN)
    return "!", 200
 
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
