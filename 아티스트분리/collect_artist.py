from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
import csv
import json
import requests
import re
import unicodedata
import urllib.request
import time
from requests import put
import pandas as pd
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import webDriverWait
# from selenium.webdriver.support import expected_condition as EC


filename = "singer.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

search_keyword = 0
artists = set()
with open('songs.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter='\t')
    # 헤더(컬럼명) 건너뛰고 싶을 때
    next(csvreader)
    for row in csvreader:
        row[0] = row[0].split(',')
        #row[0]=list(row[0])
        row[0][1] = row[0][1].replace('"', '')
        #print(row[0][0],row[0][1])
        #search_keyword = row[0][0]+' '+row[0][1]
        artist = row[0][1]
        locate = artist.find('(')
        if locate == -1:
            artist = artist
        else:
            artist = artist[:locate]
        artists.add(artist)

    artists = list(artists)

    for i in artists:
        payload = [i]
        # print(i)
        writer.writerow(payload)
