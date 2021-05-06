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

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()
# browser.quit()
url_daum = "https://www.daum.net/"
url_naver = "https://www.naver.com/"
url_google = "https://www.google.co.kr/"
url_melon = "https://www.melon.com/"

filename = "solo_or_group.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
g='그룹'
s='솔로'
search_keyword=0
#artists=set()
browser.get(url_melon)
with open('singer.csv', 'r') as f:
    csvreader = csv.reader(f)
    # 헤더(컬럼명) 건너뛰고 싶을 때
    #next(csvreader)
    for row in csvreader:
        elem = browser.find_element_by_xpath("//*[@id='top_search']")
        print(type(row[0]))
        print(row[0])
        payload=[]
        payload.append(row[0])
        elem.send_keys(row[0])
        #elem.submit()
        elem.send_keys(Keys.RETURN)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        flag = soup.find('dl', attrs={'class': 'info_02 clfix'})
        if flag==None:
            elem = browser.find_element_by_xpath("//*[@id='top_search']")
            elem.clear()
            browser.back()
            continue
        print(flag.find_all('dd')[1].get_text())
        line = flag.find_all('dd')[1].get_text()
        elem = browser.find_element_by_xpath("//*[@id='top_search']")
        elem.clear()
        try:
            if line.find(s)!=-1:
                payload.append(s)
                writer.writerow(payload)
                elem.clear()
                browser.back()
                continue
            elif line.find(g)!=-1:
                payload.append(g)
                writer.writerow(payload)
                elem.clear()
                browser.back()
                continue
            else:
                payload.append(" ")
                writer.writerow(payload)
                elem.clear()
                browser.back()
                continue
        except:
            browser.quit() 


       
