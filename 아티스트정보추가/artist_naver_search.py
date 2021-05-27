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
with open('fg.csv', 'r', encoding="utf-8-sig") as file:
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
            # browser.implicitly_wait(0.2)
            elem = browser.find_element_by_xpath("//*[@id='nx_query']")
            html = browser.page_source
            soup = BeautifulSoup(html, "lxml")
            payload.append(row[0])
            try:
                group = soup.find(
                        'div', attrs={'class': 'who'})
                # elem.clear()
                flag=group.get_text()
                # flag.find('뮤지컬배우') != -1 or flag.find('가수') != -1 or flag.find('음악인') != -1:
                if flag.find('뮤지컬배우') != -1 or flag.find('가수') != -1 or flag.find('음악인') != -1:
                    # browser.find_element_by_xpath("//*[@id='content']/div/div[2]/div[2]/div/div/div/div/a").click()
                    # browser.implicitly_wait(0.3)
                    WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div")))
                    elem = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div[2]/div[2]/div/div/div/div/a")))
                    elem.click()
                    WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div/div[4]/dl")))
                    html = browser.page_source
                    soup = BeautifulSoup(html, "lxml")
                    member = soup.find('dl', {"class": "dsc"}).dd
                    payload.append(member.get_text())
                    # for sibling in soup.find('dl', {"class": "dsc"}).dd.a.next_siblings:
                    #     members = sibling.get_text()
                    #     payload.append(members)
                    #     print(members+" ")
                    print(member.get_text())
                    writer.writerow(payload)
                else:
                    print('NULL')
                    payload.append('NULL')
                    writer.writerow(payload)
                    continue
            except Exception as e:
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
