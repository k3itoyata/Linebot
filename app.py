from test10 import ras


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import glob
import datetime
import json
import csv
from dataclasses import replace
import re
import numpy as np
from pathlib import Path
import nyusu
import scw 
import os
import requests
import pprint
import urllib.request
from bs4 import BeautifulSoup
import test10
import yotei


line_bot_api = LineBotApi('bQcAlNXxwmjINfG8jFAdWcsAj8o0k9cseC1zPiLZyJgDAoJOpHjpiYOvs0wzLuvnbb7gQC9DChens1wBX0FyKtXKHfTPj/MZjfxJpxT44rsE7x1NWpfT4fTaszZ+qFT2TUYQdo+4F7XoOus+bj/24AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2ff241c4d4eb6e6c18018f4f8b6c43a5')

app = Flask(__name__)

@app.route("/")
def say_hello():
    return "Hello"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    text_in = event.message.text
    if "今日の天気" in text_in: 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=scw.getw()))
    elif "明日の天気" in text_in:   
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=scw.tom_getw()))
    elif "ニュース" in text_in :
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=nyusu.nyu()))
    elif "出席" in text_in:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=test10.mondo()))
    elif "予定登録" in text_in:
        
        yotei,day=text_in.split(",", 1)
        day=day.split(",")
        day= [int(d) for d in day]
        f = open(f'yotei/yotei{str(day[3])}.csv' ,'w')
        data = [str(yotei),str(day)]
        writer = csv.writer(f)
        writer.writerows(data)
        f.close()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=yotei.yotei()))
        
    mondo = ras(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= mondo))


if __name__ == "__main__":
    app.run()