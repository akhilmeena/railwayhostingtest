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

user_dict = {}
class User:
    def __init__(self, header):
        self.header = header
        self.pic = pic

img1 = "AgACAgEAAxkBAAIO8mCypXXkjdOW73gvA1bJJVAOp-3AAAJPqTEb4O2JRSSlsgxXnWCMUl6tSxcAAwEAAwIAA3kAA3DMAQABHwQ"
img2 = "AgACAgEAAxkBAAIO9GCypY5EUYJBbzWAjKO0lQP7cU3kAAJQqTEb4O2JRRW0fV_lS3DGDpgwTBcAAwEAAwIAA3kAAy1JAgABHwQ"
img3 = "AgACAgEAAxkBAAIO9mCypZMrk62fq3uAqaXi2SBxc6n-AAJRqTEb4O2JRV7mVu-ZPRc2pbI2TBcAAwEAAwIAA3kAA9f8AAIfBA"
img4 = "AgACAgEAAxkBAAIO-GCypZxrqyMrlKQSaWjIqTDfeh21AAIIqTEbEy4ZRK4zbKSALKmj9A8vTBcAAwEAAwIAA3gAA-a1AQABHwQ"
img5 = "AgACAgEAAxkBAAIO-mCypZ7e82MaViHULxxNmRziQqW5AAICqjEbVjVwRDPj2mBn7FplI2kSTRcAAwEAAwIAA3gAA0xKAAIfBA"
img6 = "AgACAgEAAxkBAAIO_GCypaECbj8J8h5wdzFRd0nBq1ibAAL6qTEbVjVwRNvHO25MtKyYwoDwSxcAAwEAAwIAA20AA95eAQABHwQ"
img7 = "AgACAgEAAxkBAAIO_mCypaejSpsoEU2a56icEk-1RXwCAAKGqTEbojGRRWCFDvr_jVsLDYktTBcAAwEAAwIAA3gAA4g9AgABHwQ"
img8 = "AgACAgEAAxkBAAIPAAFgsqWrho7D-3jc6HjasbaDbFEXbAACiKkxG6IxkUUtdmxoXK_qfF4Gc0oXAAMBAAMCAAN5AAOCAAEEAAEfBA"
img9 = "AgACAgEAAxkBAAIPAmCypbCKj0B_ZpGmXDB9qUA358dyAAL2qTEbVjVwRIk6foOdc8KOBufDShcAAwEAAwIAA3gAA-pfAgABHwQ"
img10 = "AgACAgEAAxkBAAIPBmCypbvlgQeUKhZqVtL0BFo5LRjAAALtqDEbah8gRHio7L47g8qZr3vIShcAAwEAAwIAA3kAA4E7AgABHwQ"
img11 = "AgACAgEAAxkBAAIPBGCypbilegypgnlvLN3-s1sQJrWKAAJYqTEbUMeIRcrrme1k0V8-mxodTRcAAwEAAwIAA3kAA22kAAIfBA"
img12 = "AgACAgEAAxkBAAIPCGCypb8vP5yNzRejDVQkfCkW0gVhAAKHqTEbojGRRdd0JJ2acm1pHPvuSxcAAwEAAwIAA3kAAzXQAQABHwQ"
img13 = "AgACAgEAAxkBAAIPCmCypcb3CVM4lUO0IrI1GA9x_pnNAAJqqTEbExoxRH4XWsFE3DQnq-zrSxcAAwEAAwIAA3gAAz9jAQABHwQ"
img14 = "AgACAgEAAxkBAAIPDGCypckAAV5MpVsO8sr0DPG5zWpKxgACiakxG6IxkUUymPznU5pBD7oKGk0XAAMBAAMCAAN5AAMqpAACHwQ"
img15 = "AgACAgEAAxkBAAIPDmCypcxWES7kERb0vjW04BolzoyzAAILqTEbweCJRc9zMF1-XPqtcxZ2ShcAAwEAAwIAA3kAA9nxAwABHwQ"
img16 = "AgACAgEAAxkBAAIPEGCypdDij522VhDVUl-fzJEmA_JbAAKKqTEbojGRRWYsf6n0CvFqtyUgTRcAAwEAAwIAA3kAA66xAAIfBA"
img17 = "AgACAgEAAxkBAAIPEmCypdQfX1bwXk0yQwLbaAPwrjT4AAJVqjEbyQEwRJ4Xy79MxPeZ2pbOShcAAwEAAwIAA3kAAyAzAgABHwQ"
img18 = "AgACAgEAAxkBAAIPFGCypdxUNvhSS5vDPHagWszmLLY_AALzqDEbExo5RB7ZeEgqlHZBZP8WTRcAAwEAAwIAA3kAA5AzAAIfBA"
img19 = "AgACAgEAAxkBAAIPFmCypeCtxYjBxmnHxD0l7UB6o3LqAAJTqjEbyQEwRG9UsmyrsRt6fezrSxcAAwEAAwIAA3kAA7trAQABHwQ"
img20 = "AgACAgEAAxkBAAIPGGCypeO0LMZQRZej0OZ6apIj4emHAAJbqTEbB-CJR3NG4sj2r9giQfy0SxcAAwEAAwIAA3kAA68eAQABHwQ"
img21 = "AgACAgEAAxkBAAIPGmCypeZACVXWm0OlxGLn7s4hk7HjAAIsqTEbExoxRKPY7jhpae2a53nIShcAAwEAAwIAA3kAA6tGAgABHwQ"
img22 = "AgACAgEAAxkBAAIPHGCypeze5jvGQs_HXXbHP0Mk-fyWAAK-qjEbktiBR95AtSiX_1C_sJcwTBcAAwEAAwIAA3kAA-OdAQABHwQ"
img23 = "AgACAgEAAxkBAAIPHmCypfWcv5A3adWCxPmA64wpYalbAAIrqTEbktiJR-zZ-TNHmrVvZA8vTBcAAwEAAwIAA3gAA-CDAQABHwQ"
img24 = "AgACAgEAAxkBAAIPIGCypffMdvJgyx_Xn4ftc7Mqg2a0AAJ2qTEbB-CJRyqXvqB60rfmCYjLShcAAwEAAwIAA3gAA241AgABHwQ"
img25 = "AgACAgEAAxkBAAIPImCypfrMOGuNEVcxUORYU17SjxN2AAJXqTEbUMeIRQ3NK3hhZk5QDErkSxcAAwEAAwIAA3kAA9a8AQABHwQ"
img26 = "AgACAgEAAxkBAAIPJGCypf3uQ3evX7Tv2rUkjR-ZQ1WGAAJ4qTEbB-CJR-49NX6NpMwYoXezSxcAAwEAAwIAA3gAA8IuAQABHwQ"
img27 = "AgACAgEAAxkBAAIPJmCypgHaMlu6XJroe2Qp8Wpm9QFSAAI4qTEbojGZRQMs1XMbwgwDczc4TBcAAwEAAwIAA20AA3HwAAIfBA"
img28 = "AgACAgEAAxkBAAIPKGCypgTbuDJIq4mcXuW_jbjBBZrGAAJ_qTEbB-CJR2wfifGdM-RojHAnTBcAAwEAAwIAA3gAA-ClAQABHwQ"
img29 = "AgACAgEAAxkBAAIPKmCypgfI8tptafRr089D3jCPDGqwAAJ8qTEbB-CJR41AMhbZ4xde-I7zSxcAAwEAAwIAA3gAA_MiAQABHwQ"
img30 = "AgACAgEAAxkBAAIPLGCypgzhgfsZM4PCwPAX7zmwXHnHAAJcqTEbB-CJR-O2cC3klOhAv-rrSxcAAwEAAwIAA3gAA0UwAQABHwQ"

lnk1 = "https://kuklink.com/1/bnYyZDBwMDAwMDk4"
lnk2 = "https://kuklink.com/1/bnYyZDBwMDA1cmRy"
lnk3 = "https://kuklink.com/1/bnYyZDBsMDAyajBk"
lnk4 = "https://kuklink.com/1/bnYyZDBsMDAxczF5"
lnk5 = "https://kuklink.com/1/bnYyZDBoMDAwNHhq"
lnk6 = "https://kuklink.com/1/bnYyZDBoMDAwOHJk"
lnk7 = "https://kuklink.com/1/bnYyZDBoMDAwMDdw"
lnk8 = "https://kuklink.com/1/bnYyZDA5MDAwcGRm"
lnk9 = "https://kuklink.com/1/bnYyZDA5MDAwZDE5"
lnk10 = "https://kuklink.com/1/bnYyZDAxMDA1MXRi"
lnk11 = "https://kuklink.com/1/bnYyZDAxMDAxZ3l5"
lnk12 = "https://kuklink.com/1/bnYyZDAxMDA1OHJr"
lnk13 = "https://kuklink.com/1/bnYyY3p0MDAxZ29v"
lnk14 = "https://kuklink.com/1/bnYyY3p0MDAxc3Rj"
lnk15 = "https://kuklink.com/1/bnYyY3pwMDAwdnpu"
lnk16 = "https://kuklink.com/1/bnYyZDAxMDAxZ3l5"
lnk17 = "https://kuklink.com/1/bnYyZDAxMDA1OHJr"
lnk18 = "https://kuklink.com/1/bnYyY3p0MDAxZ29v"
lnk19 = "https://kuklink.com/1/bnYyY3p0MDAxc3Rj"
lnk20 = "https://kuklink.com/1/bnYyY3pwMDAwdnpu"
lnk21 = "https://kuklink.com/1/bnYyY3pwMDAwZGR4"
lnk22 = "https://kuklink.com/1/bnYyY3psMDAwdTM3"
lnk23 = "https://kuklink.com/1/bnYyY3psMDAyZXNx"
lnk24 = "https://kuklink.com/1/bnYyY3psMDAxbm41"
lnk25 = "https://kuklink.com/1/bnYyY3psMDAwejg3"
lnk26 = "https://kuklink.com/1/bnYyY3psMDAwajY2"
lnk27 = "https://kuklink.com/1/bnYyY3psMDAwMXQy"
lnk28 = "https://kuklink.com/1/bnYyY3pkMDAzOTI3"
lnk29 = "https://kuklink.com/1/bnYyY3pkMDAwZHZt"
lnk30 = "https://kuklink.com/1/bnYyY3o5MDA1N2h1"

titlle1 = "बदमाश भाभी जी ने हर किसी को घर बुलाकर मज़ा लिया"
titlle2 = "पति के बाहर जाते ही भाभी जी को देवर ने बिन कं*डोम लगाए पे*ल दिया"
titlle3 = "Bossgirlannie Paid App Hot Live Video - 1 😍💦"
titlle4 = "दोस्त की गर्लफ्रेंड के साथ मज़ा लेकर चु*दाई का आनंद लिया"
titlle5 = "cute 🥰 tamil girl hard tapatap with bf 😍😍"
titlle6 = "👙Indian Boss F#¢king His Office Two Girls।🤭🤭    "
titlle7 = "अपने भाई जैसे दोस्त की बहन को "
titlle8 = "Massage Rooms Hot brunette has squirting orgasm before good👙🤩"
titlle9 = "बॉयफ्रेंड ने की गार्डन मै गर्लफ्रेंड के साथ चु#ड़ाई वीडियो हुई वायरल💦"
titlle10 = "s€xy girl gone mad with his boyfriend"
titlle11 = "👙नौकरानी की लड़की जब उसकी जगह काम पे आई तो मकान मालिक ने जम कर किए हात साफ💦"
titlle12 = "टीचर नें देसी लड़की से लं*ड चुसवाकर जबरदस्त चो*दा👙💦"
titlle13 = "Ladki ko itna bhynkar ch#da ki drd se chilane lgi👙🤩"
titlle14 = "👙सुहाग रात पर भाभी की दर्द नाक चू#दाई💦"
titlle15 = "Malik ne servant ko kitchen m hi chod@ dekhye👙🤩"
titlle16 = "बदमाश भाभी जी ने हर किसी को घर बुलाकर मज़ा लिया"
titlle17 = "पति के बाहर जाते ही भाभी जी को देवर ने बिन कं*डोम लगाए पे*ल दिया"
titlle18 = "Bossgirlannie Paid App Hot Live Video - 1 😍💦"
titlle19 = "दोस्त की गर्लफ्रेंड के साथ मज़ा लेकर चु*दाई का आनंद लिया"
titlle20 = "cute 🥰 tamil girl hard tapatap with bf 😍😍"
titlle21 = "👙Indian Boss F#¢king His Office Two Girls।🤭🤭    "
titlle22 = "अपने भाई जैसे दोस्त की बहन को "
titlle23 = "Massage Rooms Hot brunette has squirting orgasm before good👙🤩"
titlle24 = "बॉयफ्रेंड ने की गार्डन मै गर्लफ्रेंड के साथ चु#ड़ाई वीडियो हुई वायरल💦"
titlle25 = "s€xy girl gone mad with his boyfriend"
titlle26 = "👙नौकरानी की लड़की जब उसकी जगह काम पे आई तो मकान मालिक ने जम कर किए हात साफ💦"
titlle27 = "टीचर नें देसी लड़की से लं*ड चुसवाकर जबरदस्त चो*दा👙💦"
titlle28 = "Ladki ko itna bhynkar ch#da ki drd se chilane lgi👙🤩"
titlle29 = "👙सुहाग रात पर भाभी की दर्द नाक चू#दाई💦"
titlle30 = "Malik ne servant ko kitchen m hi chod@ dekhye👙🤩"

        
@bot.message_handler(commands=['start'])
def test(m):
  bot.send_message(m.chat.id,text="akhill")

@bot.message_handler(commands=['getimg'])
def getimgid(m):
  m = bot.send_message(m.chat.id,text="send me pics")
  bot.register_next_step_handler(m, getid)

def getid(m):
  try:
    photo_id = m.photo[-1].file_id
    m = bot.send_message(m.chat.id,text=photo_id)
    bot.register_next_step_handler(m, getid)
  except:
    bot.send_message(m.chat.id,text="send it again /start")

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
      bot.send_photo(chat_id="-1001246111561",photo=f'{photo1}',caption=f"{caption1}",parse_mode="html")
      bot.send_message(m.chat.id,text="posted")
    else:
      m = bot.send_message(m.chat.id,text="link is not valid send again pdisk Link")
      bot.register_next_step_handler(m, channel2)


@bot.channel_post_handler(func=lambda message:True, content_types=['text'])
def chatid(message):
  fnd = "✅ Watch online"
  ttt = message.text
  ak = fnd in ttt
  if f"{ak}" == "False":
    sequence = [i for i in range(30)]
    subset = sample(sequence, 3)
    for i in subset:
      ttttt = [titlle1,titlle2,titlle3,titlle4,titlle5,titlle6,titlle7,titlle8,titlle9,titlle10,titlle11,titlle12,titlle13,titlle15,titlle16,titlle17,titlle18,titlle19,titlle20,titlle21,titlle22,titlle23,titlle24,titlle25,titlle26,titlle27,titlle28,titlle29,titlle30]
      ppppp = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12,img13,img15,img16,img17,img18,img19,img20,img21,img22,img23,img24,img25,img26,img27,img28,img29,img30]
      lllll = [lnk1,lnk2,lnk3,lnk4,lnk5,lnk6,lnk7,lnk8,lnk9,lnk10,lnk11,lnk12,lnk13,lnk15,lnk16,lnk17,lnk18,lnk19,lnk20,lnk21,lnk22,lnk23,lnk24,lnk25,lnk26,lnk27,lnk28,lnk29,lnk30]
      t1 = f"🔞 " + ttttt[int(i)]
      t2 = "\n━━━━━━━━━━━━━━━━━━━━"
      t3 = f"\n📥 Download now\n{lllll[int(i)]}\n✅ Watch online \n◼️ <a href='{lllll[int(i)]}'>480p</a> 🔶 <a href='{lllll[int(i)]}'>720p</a> ◼️"
      t4= "\n━━━━━━━━━━━━━━━━━━━━"
      t5 = "\nWATCH ONLINE OR DOWNLOAD\n(Just Install PLAYit App from playstore)\n🚀 Fastest Speed || 🔆 No Buffering"
      caption1 = f"<b>{t1}{t2}{t3}{t4}{t5}</b>"
      bot.send_photo(message.chat.id,photo=f'{ppppp[int(i)]}',caption=f"{caption1}",parse_mode="html")
  else:
    print("np")
    #bot.send_message(message.chat.id,text="nothing")


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