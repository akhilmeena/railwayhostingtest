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

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credential.json", scope)
client = gspread.authorize(creds)
ak = client.open("pdiskv2")
sheet1 = ak.worksheet(Config.SHEETA)
 
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
  if f"{m.chat.id}" not in authid:
    bot.send_message(m.chat.id,text="Bot is Offline")
    break
  else:
    print("correct admin")
    continue
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
      values_list2 = sheet1.col_values(1)
      for i in values_list2:
        try:
          bot.send_photo(chat_id=f"{i}",photo=f'{photo1}',caption=f"{caption1}",parse_mode="html")
        except:
          bot.send_message(m.chat.id,text=f"{i} failed")
      chotu=bot.send_photo(chat_id=Config.CHANNEL_ID,photo=f'{photo1}',caption=f"{caption1}",parse_mode="html")
      akhil=chotu.message_id
      sheet1.update("D20",akhil)
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
      bot.forward_message(chat_id = message.chat.id, from_chat_id = Config.CHANNEL_ID, message_id = f"{pstid}")
      time.sleep(2)
  else:
    print("np")
  channel = message.chat.id
  try:
    cells = sheet1.find(f"{channel}")
    row1 = cells.row
    vitt1 = 'B' + f"{row1}"
    fllnktxtt = sheet1.cell(int(row1),2).value
    text1 = '<a href="https://t.me/joinchat/jqne_cxAZVU1ZmQ1">🔞 New Deshi Porn Movies  🔞\n🔞 New Deshi Porn Movies  🔞</a>'
    if f"{fllnktxtt}" != "":
      bot.delete_message(channel,fllnktxtt)
    else:
      print("....")
    a = bot.send_message(message.chat.id,text=f"{text1}",parse_mode="html",disable_web_page_preview=True)
    iddu = a.message_id
    #bot.send_message(channel,iddu)
    sheet1.update(vitt1,iddu)
  except Exception as e:
    print("....")
 
 
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
