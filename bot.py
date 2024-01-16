import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6568488552:AAGUd-ZIsr9EeflSgbdhIoPXSMnidRdUoPA")

API_ID = int(os.environ.get("API_ID", "24004349"))

API_HASH = os.environ.get("API_HASH", "5aabfb11c262b17d568d828a3100f296")

STRING = os.environ.get("STRING", "http://44.211.118.122")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
