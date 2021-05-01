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
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import webDriverWait
# from selenium.webdriver.support import expected_condition as EC

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()
browser.quit()
url_daum = "https://www.daum.net/"
url_naver = "https://www.naver.com/"
url_google = "https://www.google.co.kr/"
url_melon = "https://www.melon.com/"

search_keyword=0
artists=set()
browser.get(url_melon)
with open('songs_adj_jump.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter='\t')
    # 헤더(컬럼명) 건너뛰고 싶을 때
    next(csvreader)
    for row in csvreader:
        row[0]=row[0].split(',')
        #row[0]=list(row[0])
        row[0][1]=row[0][1].replace('"','')
        # print(row[0][0],row[0][1])
        #search_keyword = row[0][0]+' '+row[0][1]
        artist=row[0][1]
        locate=artist.find('(')
        if locate==-1:
            artist=artist
        else:
            artist=artist[:locate]
        artists.add(artist)
        print(artists)
        
    for i in artists:
        # elem=browser.find_element_by_xpath(
        #     "//*[@id='top_search']")
        # elem.send_keys(search_keyword)
        # elem.send_keys(Keys.RETURN)
        # html=elem.page_source
        # soup=BeautifulSoup(html,"lxml")
        print(i)
        break


        # browser.find_element_by_xpath(
        #     "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]").click()
