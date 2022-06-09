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

def yotei (text):
    yotei,day=text.split(",", 1)
    day=day.split(",")
    day= [int(d) for d in day]
    