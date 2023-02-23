from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
from config import *
import asyncio
from telethon import events
from help import *
c = requests.session()
bot_username = '@t06bot'


import os,requests,sys,re,time,random

from telethon import sync,events,TelegramClient

from time import sleep

b = "BotFather"#لاتغير

kse.start()

while True :

    try:

    	uss = "QWERTYUIOPASDFGHJKLZXCVBNMazqsxwdcefvrgbthnyjmukilop"    	eu = str("".join(random.choice(uss)for i in range(2)))

    	en = str("".join(random.choice(uss)for i in range(1)))

    	uss = (en+eu+'bot')

    	oa = requests.get(f'https://t.me/{uss}').text

    	if 'tgme_username_link' in oa:

    	   kse.send_message(b,'/newbot')

    	   kse.send_message(b,nam)

    	   kse.send_message(b,uss)

    except Exception as A:

    	text = str(A)

    	aaa = re.findall(r'\d+',text)[0]

    	text = int(aaa)

    	print(text)

    	time.sleep(text)

kse.run_until_disconnected()

Files
