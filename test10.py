import datetime

def ras(message):
    text = message.split(",", 1)
    if text[0] ==1:
        ret= mainy(text[1])
    if text[0] == 5:
        ret=mondo()
    else:
        ret="「数字,要件」で区切ってください"+\
            "1:予定登録, 2:予定確認, 3:天気, 4:ニュース, 5:出欠登録, 0:予定削除"
            
        
    return ret

    

def mondo():
    return  "出席:"+ "\n"+"[ "+ "https://forms.gle/uXYUTBYEti5ofuRm6"+ " ]"+"\n"+\
            "欠席:"+ "\n"+"[ "+ "https://forms.gle/ZgbsebUJgVLx8i3s7"+ " ]"+"\n"+\
            "AI開発情報サイト:"+ "\n"+ "[ "+ "https://sites.google.com/st.kobedenshi.ac.jp/it-info/%E3%82%AA%E3%83%B3%E3%83%A9%E3%82%A4%E3%83%B3%E6%8E%88%E6%A5%AD%E3%83%9D%E3%83%BC%E3%82%BF%E3%83%AB2022/ai%E3%83%86%E3%82%AF%E3%83%8E%E3%83%AD%E3%82%B8%E3%83%BC%E3%82%B3%E3%83%BC%E3%82%B9?authuser=0"+ " ]"

def mainy(text):
    yotei,day=text.split(",", 1)
    day=day.split(",")
    day= [int(d) for d in day]
    dt1 = datetime.datetime.today()
    dt2 = datetime.datetime(day[0],day[1],day[2])
    dt3 = dt2 - dt1
    return str(yotei) + "までは、後" + str(dt3.days) + "日後です"