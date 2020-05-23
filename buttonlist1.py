import os
import time
from flask import Flask, request
import re
import telebot
from telebot import types
import random

TOKEN = "1221370836:AAGzjvpt18Dvw2vw5hsbxE0fQS6q_1_NveY"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['test']) # welcome message handler
def send_welcome(m):
    chat_id = m.chat.id
    if chat_id in id_a:
        bot.send_message(chat_id, '☺️ Bot is running (VIP USER)')
    else:
        bot.send_message(chat_id, '☺️ Bot is running (FREE USER)')
        #bot.send_message(m.chat.id, text="☺️ Bot is running")

id_a = [818396979 ,608824855]

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
