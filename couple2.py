import os
import requests
from flask import Flask, request
import re
import time
import telebot
from telebot import types
import random


TOKEN = "1071595338:AAFAPoo4xsxgAHd-HuQC5NmjnAadlwmrkLI"
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)

user_dict = {}
class User:
    def __init__(self, header):
        self.header = header
        
#Akh =["#Hot","#Cool","#Brave"]
#Akh2=["#Penis","#Boobs","#Pussy","#Cock","#Dick" ]
#Akh3=["#Indian","#Rusian","#chinese","#African","#nepali"]

#Pk1 = random.choice(Akh)
#Pk2 = random.choice(Akh2)
#Pk3 = random.choice(Akh3)       
        
@bot.message_handler(func=lambda message:True, content_types=['photo'])
def command_default(m):
  Akh =["#Hot","#Cool","#Brave"]
  Akh2=["#Penis","#Boobs","#Pussy","#Cock","#Dick" ]
  Akh3=["#Indian","#Rusian","#chinese","#African","#nepali"]
  Pk1 = random.choice(Akh)
  Pk2 = random.choice(Akh2)
  Pk3 = random.choice(Akh3)  
  keyboard = types.InlineKeyboardMarkup()
  btn3 = types.InlineKeyboardButton(text = "FOLLOW ON INSTAGRAM ↗️", url = "Https://instagram.com/romantic.luv.feelings")
  keyboard.add(btn3)
  photo_id = m.photo[0].file_id
  bot.send_message(m.chat.id,text = photo_id)
  #bot.forward_message(chat_id = "-1001264715334", from_chat_id = "-1001331807064", message_id = "18")
  bot.forward_message(chat_id = "-1001196607237", from_chat_id = "-1001331807064", message_id = "18")
  bot.send_photo(chat_id=[ "-1001359337725"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_photo(chat_id=[ "-1001319607443"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_photo(chat_id=[ "-1001244088615"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_photo(chat_id=[ "-1001266253256"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_photo(chat_id=[ "-1001411426299"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  #bot.send_photo(chat_id=[ "-1001264715334"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup=keyboard)

@bot.message_handler(func=lambda message:True, content_types=['video'])
def command_default(m):
  Akh =["#Hot","#Cool","#Brave"]
  Akh2=["#Penis","#Boobs","#Pussy","#Cock","#Dick" ]
  Akh3=["#Indian","#Rusian","#chinese","#African","#nepali"]
  Pk1 = random.choice(Akh)
  Pk2 = random.choice(Akh2)
  Pk3 = random.choice(Akh3)  
  keyboard = types.InlineKeyboardMarkup()
  btn3 = types.InlineKeyboardButton(text = "FOLLOW ON INSTAGRAM ↗️", url = "Https://instagram.com/romantic.luv.feelings")
  keyboard.add(btn3)
  photo_id = m.video.file_id
  bot.send_message(m.chat.id,text = photo_id)
  #bot.forward_message(chat_id = "-1001264715334", from_chat_id = "-1001331807064", message_id = "18")
  bot.forward_message(chat_id = "-1001196607237", from_chat_id = "-1001331807064", message_id = "18")
  bot.send_video(chat_id=[ "-1001359337725"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_video(chat_id=[ "-1001319607443"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_video(chat_id=[ "-1001244088615"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_video(chat_id=[ "-1001266253256"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_video(chat_id=[ "-1001411426299"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  #bot.send_video(chat_id=[ "-1001264715334"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup=keyboard)

@bot.message_handler(func=lambda message:True, content_types=['document'])
def command_default(m):
  Akh =["#Hot","#Cool","#Brave"]
  Akh2=["#Penis","#Boobs","#Pussy","#Cock","#Dick" ]
  Akh3=["#Indian","#Rusian","#chinese","#African","#nepali"]
  Pk1 = random.choice(Akh)
  Pk2 = random.choice(Akh2)
  Pk3 = random.choice(Akh3)  
  keyboard = types.InlineKeyboardMarkup()
  btn3 = types.InlineKeyboardButton(text = "FOLLOW ON INSTAGRAM ↗️", url = "Https://instagram.com/romantic.luv.feelings")
  keyboard.add(btn3)
  photo_id = m.document.file_id
  bot.send_message(m.chat.id,text = photo_id)
  #bot.forward_message(chat_id = "-1001264715334", from_chat_id = "-1001331807064", message_id = "18")
  bot.forward_message(chat_id = "-1001196607237", from_chat_id = "-1001331807064", message_id = "18")
  bot.send_document(chat_id=[ "-1001359337725"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_document(chat_id=[ "-1001319607443"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_document(chat_id=[ "-1001244088615"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_document(chat_id=[ "-1001266253256"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  bot.send_document(chat_id=[ "-1001411426299"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
  #bot.send_document(chat_id=[ "-1001264715334"], data=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup=keyboard)

  
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