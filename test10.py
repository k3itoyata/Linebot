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
    
    #elif text[0]=="2":
        #ret= cpt(text[1])
    
    elif text[0] == "3":
        ret= selly()
    
    elif text[0] == "4":
        ret= zeder()
    
    elif text[0] == "5":
        ret= mondo()
    else:
        ret="「数字,要件」で区切ってください"+\
            "1:予定登録, 2:予定確認, 3:天気, 4:ニュース, 5:出欠登録, 0:予定削除"
            
        
    return ret

def mainy(text):
    yotei,day,hozon=text.split(",", 1)
    day=day.split(",")
    day= [int(d) for d in day]
    dt1 = datetime.datetime.today()
    dt2 = datetime.datetime(day[0],day[1],day[2])
    dt3 = dt2 - dt1
    return str(yotei) + "までは、後" + str(dt3.days) + "日後です"+"\n"+\
        str(hozon) + "に保存します" 



area_dic = {'兵庫県':'280000',}

    # CSV出力先
output_file = "tenki.csv"

    # CSVヘッダー
header = ["都道府県","データ配信元","地方名","予報日時","天気",]

def main():
    make_csv()

def make_csv():
    with open(output_file, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(header)

            # JSONから情報を取得
        write_lists = get_info()

            # CSV書き込み
        writer.writerows(write_lists)

def get_info():
    write_lists = []
    base_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/"
    for k, v in area_dic.items():

        if k.find("/"):
            prefecture = k[0:k.find("/")]
        else:
            prefecture = k

        url = base_url + v + ".json"

        res = requests.get(url).json()

        for re in res:
            publishingOffice = re["publishingOffice"]
            reportDatetime = re["reportDatetime"]

            timeSeries = re["timeSeries"]

            for time in timeSeries:
                    #降水確率など今回のターゲット以外は除外する
                if 'pops' in time["areas"][0]:
                    pass
                elif 'temps' in time["areas"][0]:
                    pass
                elif 'tempsMax' in time["areas"][0]:
                    pass
                else:
                    for i in range(len(time["areas"])):

                        local_name = time["areas"][i]["area"]["name"]

                        for j in range(len(timeSeries[0]["timeDefines"])):

                            if 'weathers' not in time["areas"][i]:
                                weather = ""
                            else:
                                weather = time["areas"][i]["weathers"][j]

                            if 'winds' not in time["areas"][i]:
                                wind = ""
                            else:
                                wind = time["areas"][i]["winds"][j]

                            if 'waves' not in time["areas"][i]:
                                wave = ""
                            else:
                                wave = time["areas"][i]["waves"][j]

                            timeDefine = time["timeDefines"][j]

                                # 各情報をリストに格納
                            write_list = []
                            write_list.append(prefecture)
                            write_list.append(publishingOffice)
                            write_list.append(local_name)
                            write_list.append(timeDefine)
                            write_list.append(weather)
                            write_lists.append(write_list)
    return write_lists

if __name__ == '__main__':
    main()

def selly():

    filename = 'tenki.csv'
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        for i in csvreader:
            j= [item.replace("\u3000", "") for item in i]
    return str(j).replace(",", "")

def zeder():
    URL = "https://www.yahoo.co.jp/"
    rest = requests.get(URL)

    # BeautifulSoupにヤフーニュースのページ内容を読み込ませる
    soup = BeautifulSoup(rest.text, "html.parser")

    # ヤフーニュースの見出しとURLの情報を取得して出力する
    data_list = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
    for data in data_list:
        return data.span.string + "\n"+\
               data.attrs["href"] 
def mondo():
    return  "出席:"+ "\n"+"[ "+ "https://forms.gle/uXYUTBYEti5ofuRm6"+ " ]"+"\n"+\
            "欠席:"+ "\n"+"[ "+ "https://forms.gle/ZgbsebUJgVLx8i3s7"+ " ]"+"\n"+\
            "AI開発情報サイト:"+ "\n"+ "[ "+ "https://sites.google.com/st.kobedenshi.ac.jp/it-info/%E3%82%AA%E3%83%B3%E3%83%A9%E3%82%A4%E3%83%B3%E6%8E%88%E6%A5%AD%E3%83%9D%E3%83%BC%E3%82%BF%E3%83%AB2022/ai%E3%83%86%E3%82%AF%E3%83%8E%E3%83%AD%E3%82%B8%E3%83%BC%E3%82%B3%E3%83%BC%E3%82%B9?authuser=0"+ " ]"

