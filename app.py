from test10 import ras


from flask import Flask, request, abort, render_template

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
import jyugyou
import yotei


line_bot_api = LineBotApi('EPobn2l7x8wn7aEGKrbZHqB/MMN2sHax2cd+blM2u0993YZcIIO2csK/Yjp+pUhiq6hCk3T6ez8buPtNSR49gQXAz/68TUu5D2MBIEYH74PU9/y6Zz5cNeQnaYCI21kmJRFrT5zszqaXj4emBGttywdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('984e07ab505077e9d2c34e799d2ec905')

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
    if  "今日の天気" in text_in: 
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=scw.getw()))
    elif "明日の天気" in text_in:   
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=scw.tom_getw()))
    elif "ニュース" in text_in :
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=nyusu.nyu()))
    elif "出席" in text_in:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=test10.mondo()))
    elif "月曜日" in text_in:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=jyugyou.getuyoubi()))
    elif "火曜日" in text_in:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=jyugyou.kayoubi()))
    elif "水曜日" in text_in:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=jyugyou.suiyoubi()))
    elif "木曜日" in text_in:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=jyugyou.mokuyoubi()))
    elif "金曜日" in text_in:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=jyugyou.kinyoubi()))
    elif "予定" in text_in:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=yotei.yotei()))
    elif "サブスク" in text_in:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=test10.kawase()))
    elif "なかやまきんに君" in text_in:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=test10.uruka()))
    
    mondo = ras(event.message.text)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= mondo))


if __name__ == "__main__":
    app.run()