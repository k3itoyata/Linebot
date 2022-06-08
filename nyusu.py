import glob
import datetime
import requests
import json
import csv
from dataclasses import replace
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
from pathlib import Path
import os


def nyu():

    URL = "https://www.yahoo.co.jp/"
    rest = requests.get(URL)

    # BeautifulSoupにヤフーニュースのページ内容を読み込ませる
    soup = BeautifulSoup(rest.text, "html.parser")

    # ヤフーニュースの見出しとURLの情報を取得して出力する
    data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
    for data in data_list:
        a= data.span.string 
        b= data.attrs["href"]
        x= a+ b
        return x