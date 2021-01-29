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
  try:
    photo_id = m.photo[-1].file_id
    file_path = bot.get_file(photo_id).file_path
    photo = bot.download_file(file_path)
    img = Image.open(BytesIO(photo))
    imgWidth,imgHeight = img.size
    img1 = Image.open("logocoup.png")
    im1Width,im1Height = img1.size
    #a = int(imgHeight)/2 + 10
    #b = 50
    #width, height = img1.size
    #img1 = img1.resize((width//2, height//2))
    #new_img = img1.resize((int(b),int(int(a))), Image.ANTIALIAS)
    #quality_val = 90
    #text_plate = Image.new("RGBA", (text_width, text_height), (0,0,0,0))
    #draw = ImageDraw.Draw(text_plate)
    #text_img.save("ball.png", format="png")
    if int(imgHeight) >= int(imgWidth):
      til = Image.new("RGB",(int(imgHeight),int(imgHeight)),(255,255,255))
      x = int(imgWidth)/2 
      y = int(imgHeight)/2
      z = int(y) - int(x)
      a = int(imgWidth)/4
      b = 50
      new_img = img1.resize((int(a),int(a)), Image.ANTIALIAS)
      quality_val = 100
      img.paste(new_img, (0,int(imgHeight/4)), mask=new_img)
      til.paste(img,(int(z),0))
      output = BytesIO()
      output.name = "image.jpeg"
      til.save(output, format='JPEG')
      photo1 = output.getvalue()
      bot.forward_message(chat_id = "-1001196607237", from_chat_id = "-1001331807064", message_id = "18")
      bot.send_photo(chat_id=[ "-1001359337725"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001319607443"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001244088615"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001266253256"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001411426299"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
    elif int(imgWidth) >= int(imgHeight):
      til = Image.new("RGB",(int(imgWidth),int(imgWidth)),(255,255,255))
      x = int(imgHeight)/2 
      y = int(imgWidth)/2
      z = int(y) - int(x)
      a = int(imgHeight)/3
      b = 50
      new_img = img1.resize((int(a),int(a)), Image.ANTIALIAS)
      quality_val = 100
      img.paste(new_img, (0,int(imgHeight/4)), mask=new_img)
      til.paste(img,(0,int(z)))
      output = BytesIO()
      output.name = "image.jpeg"
      til.save(output, format='JPEG')
      photo1 = output.getvalue()
      bot.forward_message(chat_id = "-1001196607237", from_chat_id = "-1001331807064", message_id = "18")
      bot.send_photo(chat_id=[ "-1001359337725"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001319607443"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001244088615"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001266253256"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001411426299"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
    elif int(imgWidth) == int(imgHeight):
      til = Image.new("RGB",(int(imgHeight),int(imgHeight)),(255,255,255))
      x = int(imgWidth)/2 
      y = int(imgHeight)/2
      z = int(y) - int(x)
      a = int(imgHeight)/5
      b = 50
      new_img = img1.resize((int(a),int(a)), Image.ANTIALIAS)
      quality_val = 100
      img.paste(new_img, (0,int(imgHeight/4)), mask=new_img)
      til.paste(img,(int(z),0))
      output = BytesIO()
      output.name = "image.jpeg"
      til.save(output, format='JPEG')
      photo1 = output.getvalue()
      bot.forward_message(chat_id = "-1001196607237", from_chat_id = "-1001331807064", message_id = "18")
      bot.send_photo(chat_id=[ "-1001359337725"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001319607443"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001244088615"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001266253256"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
      bot.send_photo(chat_id=[ "-1001411426299"], photo=photo1, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
    else:
      bot.send_message(m.chat.id,text="size is not defined")
    bot.send_message(m.chat.id,text = photo_id)
    #bot.forward_message(chat_id = "-1001264715334", from_chat_id = "-1001331807064", message_id = "18")
    #bot.forward_message(chat_id = "-1001196607237", from_chat_id = "-1001331807064", message_id = "18")
    #bot.send_photo(chat_id=[ "-1001359337725"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
    #bot.send_photo(chat_id=[ "-1001319607443"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
    #bot.send_photo(chat_id=[ "-1001244088615"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
    #bot.send_photo(chat_id=[ "-1001266253256"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
    #bot.send_photo(chat_id=[ "-1001411426299"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup = keyboard)
    #bot.send_photo(chat_id=[ "-1001264715334"], photo=photo_id, caption="💄👙❣️👌👈💦\n\n" + f"{Pk1} {Pk2} {Pk3}",reply_markup=keyboard)
  except Exception as e:
    bot.send_message(m.chat.id,e)





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