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

TOKEN = "1071595338:AAFAPoo4xsxgAHd-HuQC5NmjnAadlwmrkLI"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credential.json", scope)
client = gspread.authorize(creds)
ak = client.open("pdiskdata")
sheet1 = ak.worksheet("data")
sheet2 = ak.worksheet("normaldata")

user_dict = {}
class User:
    def __init__(self, header):
        self.header = header
        self.pic = pic

@bot.message_handler(commands=['start'])
def test(m):
  bot.send_message(m.chat.id,text="akhill")

#@bot.message_handler(commands=['start2'])
#def test(m):
  #aa = bot.send_message(m.chat.id,text="send me post ids")
  #bot.register_next_step_handler(aa,akkk)
  
def akkk(m):
  ids = m.text
  tag_split = ids.splitlines()
  for each_cn in tag_split:
    i = each_cn.strip()
    ppppp = sheet1.get(f"B{i}").first()
    time.sleep(1)
    ttttt = sheet1.get(f"C{i}").first()
    time.sleep(1)
    lllll = sheet1.get(f"D{i}").first()
    time.sleep(1)
    t1 = f"🔞 " + f"{ttttt}"
    t2 = "\n━━━━━━━━━━━━━━━━━━━━"
    t3 = f"\n📥 Download now\n{lllll}\n✅ Watch online \n◼️ <a href='{lllll}'>480p</a> 🔶 <a href='{lllll}'>720p</a> ◼️"
    t4= "\n━━━━━━━━━━━━━━━━━━━━"
    t5 = "\nWATCH ONLINE OR DOWNLOAD\n(Just Install PLAYit App from playstore)\n🚀 Fastest Speed || 🔆 No Buffering"
    caption1 = f"<b>{t1}{t2}{t3}{t4}{t5}</b>"
    bot.send_photo(chat_id="-1001393074609",photo=f'{ppppp}',caption=f"{caption1}",parse_mode="html")
    #time.sleep(random.randrange(5,10))



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
      h = sheet1.get('A1000').first()
      ri = int(h) + 1
      sheet1.update_cell(int(ri),1 ,f"{ri}")
      sheet1.update_cell(int(ri),2 ,f"{photo1}")
      sheet1.update_cell(int(ri),3 ,f"{head}")
      sheet1.update_cell(int(ri),4 ,f"{link}")
      values_list2 = sheet2.col_values(1)
      for i in values_list2:
        try:
          bot.send_photo(chat_id=f"{i}",photo=f'{photo1}',caption=f"{caption1}",parse_mode="html")
          #bot.send_message(m.chat.id,text=f"{i} posted")
        except:
          bot.send_message(m.chat.id,text=f"{i} failed")
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
    h = sheet1.get('A1000').first()
    sequence = [i for i in range(int(h))]
    subset = sample(sequence, 3)
    for i in subset:
      pstid = random.randrange(2,int(h)-1)
      bot.forward_message(chat_id = message.chat.id, from_chat_id = "-1001568299394", message_id = f"{pstid}")
      time.sleep(2)
  else:
    print("np")
  channel = message.chat.id
  try:
    cells = sheet2.find(f"{channel}")
    row1 = cells.row
    vitt1 = 'B' + f"{row1}"
    #fllnktxtt = sheet2.get(vitt1).first()
    fllnktxtt = sheet2.cell(int(row1),2).value
    text1 = '<a href="https://t.me/joinchat/jqne_cxAZVU1ZmQ1">🔞 New Deshi Porn Movies  🔞\n🔞 New Deshi Porn Movies  🔞</a>'
    if f"{fllnktxtt}" != "":
      bot.delete_message(channel,fllnktxtt)
    else:
      print("....")
    a = bot.send_message(message.chat.id,text=f"{text1}",parse_mode="html",disable_web_page_preview=True)
    iddu = a.message_id
    #bot.send_message(channel,iddu)
    sheet2.update(vitt1,iddu)
  except Exception as e:
    print("....")

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