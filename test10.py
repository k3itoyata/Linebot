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

def ras(message):
    text = message.split(",", 1)
    if text[0] =="1":
        ret= mainy(text[1])
    
    elif text[0]=="2":
        ret= cpt()
    
    elif text[0] == "3":
        ret= selly()
    
    elif text[0] == "4":
        ret= zeder()
    
    elif text[0] == "5":
        ret= mondo()
    
    elif text[0] == "6":
        ret= daruma()
        
    else:
        ret="「数字,要件」で区切ってください"+\
            "1:予定登録, 2:予定確認, 3:天気, 4:ニュース, 5:出欠登録, 0:予定削除"
            
        
    return ret

def mainy(text):
    yotei,day=text.split(",", 1)
    day=day.split(",")
    day= [int(d) for d in day]
    dt1 = datetime.datetime.today()
    dt2 = datetime.datetime(day[0],day[1],day[2])
    dt3 = dt2 - dt1

    return str(yotei) + "までは、後" + str(dt3.days) + "日後です"

def cpt():
    files = os.listdir("./yotei")
    for filename in files:
        a= np.genfromtxt("yotei/" + filename, encoding='utf8', dtype=None)
        aa=(f"{filename}:"+str(a).replace('"', ""))
        return str(aa).replace(",","")

def selly():
     #対象のサイトURL
    url = "https://tenki.jp/forecast/6/31/6310/28110/"
    #インスタンス作成
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    #対象の要素
    weather = soup.find_all("p", class_="weather-telop")
    temp = soup.find_all("dd", class_="high-temp temp")
    low_temp = soup.find_all("dd", class_="low-temp temp")
    tds = soup.select("tr.rain-probability td")
    hini = soup.find_all("h3", class_="left-style")


    tenki = hini[0].getText() + "\n\n" + weather[0].getText()
    kion = "\n最高 " + temp[0].getText()
    low_kion = "  最低 " + low_temp[0].getText()
    rain1 = "\n\n降水確率\n00-06時  " + tds[0].getText()
    rain2 = "\n06-12時  " + tds[1].getText()
    rain3 = "\n12-18時  " + tds[2].getText()
    rain4 = "\n18-24時  " + tds[3].getText()
    
    a = tenki+kion+low_kion+rain1+rain2+rain3+rain4
    return a 
def zeder():
    #対象のサイトURL
    url = "https://tenki.jp/forecast/6/31/6310/28110/"
    #インスタンス作成
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, 'html.parser')
    #対象の要素
    weather = soup.find_all("p", class_="weather-telop")
    temp = soup.find_all("dd", class_="high-temp temp")
    low_temp = soup.find_all("dd", class_="low-temp temp")
    tds = soup.select("tr.rain-probability td")
    hini = soup.find_all("h3", class_="left-style")

    tenki = hini[1].getText() + "\n\n" + weather[1].getText()
    kion = "\n最高 " + temp[1].getText()
    low_kion = "  最低 " + low_temp[1].getText()
    rain1 = "\n\n降水確率\n00-06時  " + tds[4].getText()
    rain2 = "\n06-12時  " + tds[5].getText()
    rain3 = "\n12-18時  " + tds[6].getText()
    rain4 = "\n18-24時  " + tds[7].getText()

    b = tenki+kion+low_kion+rain1+rain2+rain3+rain4
    return b
def mondo():
    return  "出席:"+ "\n"+"[ "+ "https://forms.gle/uXYUTBYEti5ofuRm6"+ " ]"+"\n"+\
            "欠席:"+ "\n"+"[ "+ "https://forms.gle/ZgbsebUJgVLx8i3s7"+ " ]"+"\n"+\
            "AI開発情報サイト:"+ "\n"+ "[ "+ "https://sites.google.com/st.kobedenshi.ac.jp/it-info/%E3%82%AA%E3%83%B3%E3%83%A9%E3%82%A4%E3%83%B3%E6%8E%88%E6%A5%AD%E3%83%9D%E3%83%BC%E3%82%BF%E3%83%AB2022/ai%E3%83%86%E3%82%AF%E3%83%8E%E3%83%AD%E3%82%B8%E3%83%BC%E3%82%B3%E3%83%BC%E3%82%B9?authuser=0"+ " ]"
def daruma():
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