import requests,random,secrets,json,os,sys
import flask
import telebot
from telebot import types
from user_agent import generate_user_agent
from config import *
import logging
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start'])
def send(message):
	program = types.InlineKeyboardButton(text='DevelopeR',url='https://t.me/MMPMMMM')
	Keyy = types.InlineKeyboardMarkup()
	Keyy.row_width = 2
	Keyy.add(program)
	first = message.chat.first_name
	bot.send_message(message.chat.id,f"*⌯ Hello {first}\n\n⌯ information Account Instagram\n\n⌯ Send UserName Account \n\n⌯ User : fdk9*",parse_mode="markdown",reply_markup=Keyy,reply_to_message_id=message.message_id)
@bot.message_handler(func=lambda m: True)
def Sufi(message):
         mg = message.text
         bot.send_message(message.chat.id, text="*⌯ Wait seconds ! .*",parse_mode="markdown")
         heade = {
      'HOST': "www.instagram.com",
      'KeepAlive' : 'True',
      'user-agent': str(generate_user_agent()),
      'Cookie': cookie,
      'ContentType' : "application/x-www-form-urlencoded",
      "X-Requested-With" : "XMLHttpRequest",
      "X-IG-App-ID": "936619743392459",
      "X-Instagram-AJAX" : "missing",
      "X-CSRFToken" : "missing",
      "Accept-Language" : "en-US,en;q=0.9"}
         url = f'https://www.instagram.com/{mg}/?__a=1'
         req_io= requests.get(url,headers=heade).text
         print(req_io)
         if "logging_page_id" in req_io:
         	req_id= requests.get(url,headers=heade).json()
         	print(req_id)
         	photo = str(req_id['graphql']['user']['profile_pic_url'])
         	name    = str(req_id['graphql']['user']['full_name'])
         	id    = str(req_id['graphql']['user']['id'])
         	followres    = str(req_id['graphql']['user']['edge_followed_by']['count'])
         	following    = str(req_id['graphql']['user']['edge_follow']['count'])
         	bio    = str(req_id['graphql']['user']['biography'])
         	re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
         	ree = re.json()
         	date = ree['data']
         	program = types.InlineKeyboardButton(text='DevelopeR',url='https://t.me/MMPMMMM')
         	Keyy = types.InlineKeyboardMarkup()
         	Keyy.row_width = 2
         	Keyy.add(program)
         	bot.send_photo(message.chat.id,photo,caption=f'''
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⌯ UserName : {mg}

⌯ Name : {name}

⌯ Followers : {followres}

⌯ Following : {following}

⌯ User id : {id}

⌯ Data : {date}
┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉
⌯ Tele : @MMPMMMM ''',reply_markup=Keyy)
         if "no-js not-logged-in " in req_io:
         	program = types.InlineKeyboardButton(text='DevelopeR',url='https://t.me/MMPMMMM')
         	Keyy = types.InlineKeyboardMarkup()
         	Keyy.row_width = 2
         	Keyy.add(program)
         	bot.send_message(message.chat.id,f'''
❌ This User is Not On Instagram\nNow Send User Agein''',reply_markup=Keyy)

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://hobot5.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
bot.polling()
