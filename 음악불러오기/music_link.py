from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# https: // search.daum.net/search?nil_suggest = btn & w = vclip & DA = STC & q = butter & CPVal = 7b479cb3

req = requests.get(f'http://www.muziker.co.kr/php/New/GetMusic.php')
data = req.json()

ytb_arr = []
num_arr = []

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")

driver = webdriver.Chrome(
    '/Users/1000ho0/Downloads/chromedriver', options=options)
# # driver = webdriver.Chrome('/Users/1000ho0/Downloads/chromedriver')
driver.implicitly_wait(3)

for title in data['response']:
    search = title['artist'].split(
        '(')[0]+' '+title['title'].split('(')[0]+' MV'
#     search = search.replace('#','')
    session = requests.Session()
    print(search)
#
#     html = session.get('https://www.google.com/search?q='+str(search),headers=header)

    driver.get(
        'https://search.daum.net/search?nil_suggest=btn&w=vclip&DA=SBC&q='+str(search))
    html = driver.page_source
#     print(html.text)
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.find_all('ul', {"class": "list_item type_list"})
#     print(count)
    if len(links) > 0:
        #         for link in links :
        link = links[0]
        link2 = link.find_all('li')
        if len(link2) > 0:
            link3 = link2[0]
            link4 = link3.find_all('div', {"class": "wrap_thumb"})
            if len(link4) > 0:
                for link5 in link4:
                    link6 = link5.find('a')
                    ytb = link6.get('href')
#                     print(ytb)
                    ytb2 = ytb.split('?v=')
                    if len(ytb2) > 1:
                        print(title['id'])
                        print(ytb2[1])
                        ytb_arr.append(ytb2[1])
                        num_arr.append(title['id'])

print('DONE')
