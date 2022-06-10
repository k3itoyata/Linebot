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

def getuyoubi():
    return "1〜3限"+"\n"+"\n"+"<zoom>"+"\n"+"https://us02web.zoom.us/j/86778775630?pwd=dkVob0w0N3FnUitPWWMvdU9kY2hndz09"+"\n"+"\n"+\
           "4〜5限"+"\n"+"\n"+"<zoom>"+"\n"+"https://us02web.zoom.us/j/86778775630?pwd=dkVob0w0N3FnUitPWWMvdU9kY2hndz09"+"\n"+"\n"+\
           "<授業スライド>"+"\n"+"https://drive.google.com/drive/u/0/folders/0B1Mo1GBJNUCNa3pueEd5cDJwekU?resourcekey=0-udrE1VQAXJwBDyxlQbm2wA"+"\n"+"\n"+\
           "<実習提出フォルダ>"+"\n"+"https://drive.google.com/drive/u/0/folders/1BzgZiq3n-R6wOItdKYrXNDAfNjPhUQTO"

def kayoubi():
    return "1〜5限"+"\n"+"\n"+"<zoom>"+"\n"+"https://us02web.zoom.us/j/87860325168?pwd=bkkyZWZuNHpxNVZyQTdPVVlia2duZz09"+"\n"+"\n"+\
            "<授業スライド>"+"\n"+"https://drive.google.com/drive/folders/1GWGkc28e-nW4qMOGS7SNUzq4gM8M9qkc?lfhs=2"

def suiyoubi():
    return "1〜3限"+"\n"+"\n"+"<zoom>"+"\n"+"https://us02web.zoom.us/j/87860325168?pwd=bkkyZWZuNHpxNVZyQTdPVVlia2duZz09"+"\n"+"\n"+\
            "<授業スライド>"+"\n"+"https://drive.google.com/drive/folders/1SoOayO7TviKbtQreRf5WCYcR7ghIFx4B?lfhs=2"+"\n"+"\n"+\
            "4〜5限"+"\n"+"\n"+"<zoom>"+"\n"+"https://us02web.zoom.us/j/87860325168?pwd=bkkyZWZuNHpxNVZyQTdPVVlia2duZz09"+"\n"+"\n"+\
             "<授業スライド>"+"\n"+"https://drive.google.com/drive/folders/11Enl6ULkeLyFnchp2nWcGYWPlB-VspnR?lfhs=2"
             
def mokuyoubi():
    return "1〜3限"+"\n"+"\n"+ "<授業補足 ＆フォローアップ>"+"\n"+"https://paper.dropbox.com/doc/AI-20222023--BfH1BLF_WQHIiq3EA7MObdOqAQ-znaDm1RdpPKzQ2rmNJ4kG"+"\n"+"\n"+\
           "4〜5限"+"\n"+"\n"+"<授業スライド>"+"\n"+"https://classroom.google.com/u/0/c/NDk5MzUzMTQ0Njk3"

def kinyoubi():
    return "1〜4限"+"\n"+"\n"+"<zoom>"+"\n"+"https://us02web.zoom.us/j/87860325168?pwd=bkkyZWZuNHpxNVZyQTdPVVlia2duZz09"+"\n"+"\n"+\
           "<授業スライド>"+"\n"+"https://classroom.google.com/u/0/c/NDk5MTg3MzYzMTU3?hl=ja"+"\n"+"\n"+\
           "5限"+"\n"+"\n"+"<zoom>"+"\n"+"https://us02web.zoom.us/j/87860325168?pwd=bkkyZWZuNHpxNVZyQTdPVVlia2duZz09"+"\n"+"\n"+\
           "<授業スライド>"+"\n"+"https://classroom.google.com/u/0/c/NDk5MzUzMTQ0Njk3"