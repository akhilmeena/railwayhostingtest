import telebot
import os
import requests
from flask import Flask, request
import re
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import html5lib
import urllib , urllib.request, http.cookiejar
from PIL import Image , ImageDraw, ImageFont
from io import BytesIO
import datetime
import calendar
import random

 
TOKEN = "1221370836:AAGzjvpt18Dvw2vw5hsbxE0fQS6q_1_NveY"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

user_dict = {}
class User:
    def __init__(self, header):
        self.header = header
        self.pic = pic
        hn
        
        
@bot.message_handler(commands=['start'])
def test(m):
  name = m.from_user.first_name
  user_id = m.from_user.username
  keyboard = types.InlineKeyboardMarkup()
  #num1 = random.randint(0, 9)
  #numvr =  num1
  #callll = types.InlineKeyboardButton(text= f"☺️ ( {numvr} )", callback_data=".")
  callback_btn1 = types.InlineKeyboardButton(text=" without pic ", callback_data="text")
  callback_btn2 = types.InlineKeyboardButton(text=" with pic ", callback_data="pic")
  #keyboard.add(callll)
  keyboard.add(callback_btn1)
  keyboard.add(callback_btn2)
  #bot.send_message(m.chat.id,text=num1)
  bot.send_message(m.chat.id,text="<b>Hey 😀   </b>" +  f'<code>{name}</code>' + f'(@{user_id})' + " <b>  how you want to send post</b>",reply_markup=keyboard,parse_mode="HTML")
  
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.message:
		if call.data == "text":
		  msg = bot.send_message(chat_id=call.message.chat.id,text="<b>send me shaayri</b>",parse_mode="HTML")
		  bot.register_next_step_handler(msg,text_sh)
		if call.data == "pic":
		  m=bot.send_message(chat_id=call.message.chat.id,text="<b>send the pic which you want to post</b>",parse_mode="HTML")
		  bot.register_next_step_handler(m,pic_send)
		if call.data == "send":
		  name = call.from_user.first_name
		  user_id = call.from_user.username
		  pic_id = User.pic
		  keyboard = types.InlineKeyboardMarkup()
		  num = random.randint(400, 1200)
		  num1 = random.randint(200, 800)
		  num2 = random.randint(500, 1500)
		  numvr =  num
		  numvr1 = num1
		  numvr2 = num2
		  call1 = types.InlineKeyboardButton(text= f"❤️ ( {numvr} )", callback_data="alert")
		  call2 = types.InlineKeyboardButton(text= f"🙏 ( {numvr1} )", callback_data="alert")
		  call3 = types.InlineKeyboardButton(text= f"😘 ( {numvr2} )", callback_data="alert")
		  btn3 = types.InlineKeyboardButton(text="😇 हिंदी पहेलिया ही पहेलिया 😇", url="https://t.me/joinchat/AAAAAFQrz4fe2Ft8UlIhPA")
		  btn4 = types.InlineKeyboardButton(text="😝 देशी MEMES & JOKES 😂", url="https://t.me/joinchat/AAAAAEdp2HJAV9_-PK8NHg")
		  keyboard.add(call1,call2,call3)
		  keyboard.add(btn3)
		  keyboard.add(btn4)
		  keybo = types.InlineKeyboardMarkup()
		  callback_btn1 = types.InlineKeyboardButton(text=" without pic ", callback_data="text")
		  callback_btn2 = types.InlineKeyboardButton(text=" with pic ", callback_data="pic")
		  keybo.add(callback_btn1)
		  keybo.add(callback_btn2)
		  bot.forward_message(chat_id = "-1001433305014", from_chat_id = "-1001163396707", message_id = "7")
		  bot.send_photo(chat_id = "-1001433305014",photo=pic_id,caption = "<b>@Shayari_Dil_Se_K\n💙💚💛💜🖤💗\n\nCredit: </b>" + f'<code>{name}</code>' + f'(@{user_id})' ,reply_markup=keyboard, parse_mode="HTML" )
		  bot.send_message(call.message.chat.id,text="<b>shayari posted to channel , now post new shayari</b>",reply_markup=keybo,parse_mode="HTML")
		if call.data == "capt":
		  m=bot.send_message(chat_id=call.message.chat.id,text = " <b>Now se nd me your caption</b>",parse_mode="HTML")
		  bot.register_next_step_handler(m,post_w)
		if call.data == "alert":
		  bot.answer_callback_query(callback_query_id=call.id, show_alert=True , text="You are not authorized to vote here.",)

def text_sh(m):
  name = m.from_user.first_name
  user_id = m.from_user.username
  User.header = m.text
  keyboard = types.InlineKeyboardMarkup()
  num = random.randint(400, 1200)
  num1 = random.randint(200, 800)
  num2 = random.randint(500, 1500)
  numvr =  num
  numvr1 = num1
  numvr2 = num2
  call1 = types.InlineKeyboardButton(text= f"❤️ ( {numvr} )", callback_data="alert")
  call2 = types.InlineKeyboardButton(text= f"🙏 ( {numvr1} )", callback_data="alert")
  call3 = types.InlineKeyboardButton(text= f"😘 ( {numvr2} )", callback_data="alert")
  btn3 = types.InlineKeyboardButton(text="😇 हिंदी पहेलिया ही पहेलिया 😇", url="https://t.me/joinchat/AAAAAFQrz4fe2Ft8UlIhPA")
  btn4 = types.InlineKeyboardButton(text="😝 देशी MEMES & JOKES 😂", url="https://t.me/joinchat/AAAAAEdp2HJAV9_-PK8NHg")
  keyboard.add(call1,call2,call3)
  btn3 = types.InlineKeyboardButton(text="😇 हिंदी पहेलिया ही पहेलिया 😇", url="https://t.me/joinchat/AAAAAFQrz4fe2Ft8UlIhPA")
  btn4 = types.InlineKeyboardButton(text="😝 देशी MEMES & JOKES 😂", url="https://t.me/joinchat/AAAAAEdp2HJAV9_-PK8NHg")
  keyboard.add(btn3)
  keyboard.add(btn4)
  keybo = types.InlineKeyboardMarkup()
  callback_btn1 = types.InlineKeyboardButton(text=" without pic ", callback_data="text")
  callback_btn2 = types.InlineKeyboardButton(text=" with pic ", callback_data="pic")
  keybo.add(callback_btn1)
  keybo.add(callback_btn2)
  bot.forward_message(chat_id = "-1001433305014", from_chat_id = "-1001163396707", message_id = "7")
  bot.send_message(chat_id = "-1001433305014",text= f"<b>{User.header}</b>" + "\n\n <b>@Shayari_Dil_Se_K\n 💙💚💛💜🖤💗\n\nCredit: </b>" + f'<code>{name}</code>' + f'(@{user_id})',reply_markup=keyboard, parse_mode = "HTML")
  bot.send_message(m.chat.id,text= f"<b>{User.header}</b>" + "\n\n <b>@Shayari_Dil_Se_K\n💙💚💛💜🖤💗\n\nCredit: </b>" + f'<code>{name}</code>' + f'(@{user_id})' ,reply_markup=keyboard, parse_mode = "HTML")
  bot.send_message(m.chat.id,text="<b>shayari posted to channel , now post new shayari</b>",reply_markup=keybo,parse_mode="HTML")
  
def pic_send(m):
  if m.content_type == "photo":
    name = m.from_user.first_name
    user_id = m.from_user.username
    pic_id = m.photo[0].file_id
    User.pic = pic_id
    keyboard = types.InlineKeyboardMarkup()
    callback_btn1 = types.InlineKeyboardButton(text=" add caption", callback_data="capt")
    callback_btn2 = types.InlineKeyboardButton(text=" post now ", callback_data="send")
    keyboard.add(callback_btn1)
    keyboard.add(callback_btn2)
    bot.send_photo(m.chat.id,photo=pic_id,caption =  "<b>@Shayari_Dil_Se_K\n 💙💚💛💜🖤💗\n\nCredit: </b>" + f'<code>{name}</code>' + f'(@{user_id})',reply_markup=keyboard, parse_mode="HTML" )
  
def post_w(m):
  name = m.from_user.first_name
  user_id = m.from_user.username
  User.capet = m.text
  pic_id = User.pic
  keyboard = types.InlineKeyboardMarkup()
  num = random.randint(400, 1200)
  num1 = random.randint(200, 800)
  num2 = random.randint(500, 1500)
  numvr =  num
  numvr1 = num1
  numvr2 = num2
  call1 = types.InlineKeyboardButton(text= f"❤️ ( {numvr} )", callback_data="alert")
  call2 = types.InlineKeyboardButton(text= f"🙏 ( {numvr1} )", callback_data="alert")
  call3 = types.InlineKeyboardButton(text= f"😘 ( {numvr2} )", callback_data="alert")
  btn3 = types.InlineKeyboardButton(text="😇 हिंदी पहेलिया ही पहेलिया 😇", url="https://t.me/joinchat/AAAAAFQrz4fe2Ft8UlIhPA")
  btn4 = types.InlineKeyboardButton(text="😝 देशी MEMES & JOKES 😂", url="https://t.me/joinchat/AAAAAEdp2HJAV9_-PK8NHg")
  keyboard.add(call1,call2,call3)
  btn3 = types.InlineKeyboardButton(text="😇 हिंदी पहेलिया ही पहेलिया 😇", url="https://t.me/joinchat/AAAAAFQrz4fe2Ft8UlIhPA")
  btn4 = types.InlineKeyboardButton(text="😝 देशी MEMES & JOKES 😂", url="https://t.me/joinchat/AAAAAEdp2HJAV9_-PK8NHg")
  keyboard.add(btn3)
  keyboard.add(btn4)
  keybo = types.InlineKeyboardMarkup()
  callback_btn1 = types.InlineKeyboardButton(text=" without pic ", callback_data="text")
  callback_btn2 = types.InlineKeyboardButton(text=" with pic ", callback_data="pic")
  keybo.add(callback_btn1)
  keybo.add(callback_btn2)
  bot.forward_message(chat_id = "-1001433305014", from_chat_id = "-1001163396707", message_id = "7")
  bot.send_photo(chat_id = "-1001433305014", photo = pic_id, caption = f"<b>{User.capet}</b>" + "\n\n<b>@Shayari_Dil_Se_K\n 💙💚💛💜🖤💗\n\nCredit: </b>" + f'<code>{name}</code>' + f'(@{user_id})',reply_markup=keyboard, parse_mode="HTML" )
  bot.send_photo(chat_id = call.message.chat.id, photo = pic_id, caption = f"<b>{User.capet}</b>" + "\n\n<b>@Shayari_Dil_Se_K\n 💙💚💛💜🖤💗\n\nCredit: </b>" + f'<code>{name}</code>' + f'(@{user_id})',reply_markup=keyboard, parse_mode="HTML" )
  bot.send_message(m.chat.id,text="<b>shayari posted to.channel, now post new shayari</b>" , reply_markup=keybo,parse_mode="HTML")	
  
  
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
