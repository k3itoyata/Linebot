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
    return "1〜3限"+"\n"+"<zoom>"+"\n"+"https://us02web.zoom.us/j/86778775630?pwd=dkVob0w0N3FnUitPWWMvdU9kY2hndz09"+"\n"+"\n"+\
           "4〜5限"+"\n"+"<zoom>"+"\n"+"https://us02web.zoom.us/j/86778775630?pwd=dkVob0w0N3FnUitPWWMvdU9kY2hndz09"+"\n"+"\n"+\
           "<授業スライド>"+"\n"+"https://drive.google.com/drive/u/0/folders/0B1Mo1GBJNUCNa3pueEd5cDJwekU?resourcekey=0-udrE1VQAXJwBDyxlQbm2wA"+"\n"+\
           "<実習提出フォルダ>"+"\n"+"https://drive.google.com/drive/u/0/folders/1BzgZiq3n-R6wOItdKYrXNDAfNjPhUQTO"
    