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
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import webDriverWait
# from selenium.webdriver.support import expected_condition as EC

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()
# browser.quit()
filename = "summary.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
search_keyword = 0
#artists=set()
# browser.get(
#     'https://people.search.naver.com/')
with open('singer_name.csv', 'r', encoding="utf-8-sig") as file:
    csvreader = csv.reader(file)
    # 헤더(컬럼명) 건너뛰고 싶을 때
    #next(csvreader)
    try:
        for row in csvreader:
            payload = []
            browser.get(
                "https://people.search.naver.com/")
            elem = browser.find_element_by_xpath("//*[@id='nx_query']")
            print('검색:'+row[0])
            elem.send_keys(str(row[0]))
            elem.send_keys(Keys.RETURN)
            elem = browser.find_element_by_xpath("//*[@id='nx_query']")
            html = browser.page_source
            soup = BeautifulSoup(html, "lxml")
            try:
                for profile, link in zip(soup.find_all('div', attrs={'class': 'profile'}), soup.find_all('div', attrs={'class': 'profile'}).div.a.attrs['href']):
                    print('e1')
                    job = profile.get_text()
                    print('e1')
                    #job.find('뮤지컬배우') != -1 or job.find('가수') != -1 or job.find('음악인') != -1:
                    
                    if job.find('뮤지컬배우') != -1 or job.find('가수') != -1 or job.find('음악인') != -1:
                        payload.append(row[0])
                        print(str(link))
                        browser.get(str(link))
                        html = browser.page_source
                        soup = BeautifulSoup(html, "lxml")
                        member = soup.find('dl', {"class": "dsc"}).dd
                        payload.append(member.get_text())
                        print(member.get_text())
                        writer.writerow(payload)
                        break
                    else:
                        print('NULL')
                        continue
            except Exception as e:
                payload.append(row[0])
                print('NULL')
                payload.append('NULL')
                writer.writerow(payload)
                print(e)
                continue

    except Exception as e:
        print(e)

        # payload.append(row[0])
        # members=group.get_text()
        # payload.append(members)
        # print(members)
        # writer.writerow(payload)
