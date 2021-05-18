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

filename = "artist_Naver_info.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
search_keyword = 0
#artists=set()
browser.get(
    'https: // people.search.naver.com/search.naver?sm=tab_hty & where=nexearch & query= & ie=utf8 & x=0 & y=0')
with open('singer_name.csv', 'r') as file:
    csvreader = csv.reader(file)
    # 헤더(컬럼명) 건너뛰고 싶을 때
    #next(csvreader)
    for row in csvreader:
        driver.get(
            "https://people.search.naver.com/search.naver?sm=sbx_hty&where=nexearch&ie=utf8&query={}&x=0&y=0".format(row[0]))
        # elem = browser.find_element_by_xpath("//*[@id='nx_query']")
        #print(type(row[0]))
        print('검색:'+row[0])
        payload = []
        elem.send_keys(row[0])
        #elem.submit()
        elem.send_keys(Keys.RETURN)
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")

        flag1 = soup.find('span', attrs={'class': 'result_profile'})
        flag2 = soup.find('span', attrs={'class': "result_profile"})
        if flag2 == None:
            elem = browser.find_element_by_xpath("//*[@id='nx_query']")
            elem.clear()
            continue

        line1 = flag2.get_text()
        line = flag2.get_text()
        # line=line.replace('/','\t')
        decision=line1.find('가수')
        if decision!=-1:
            browser.find_element_by_xpath("//*[@id='content']/div/div[2]/div[2]/div/div/a").click()
        else:

            continue




        print(line1)
        print(line)
        print('\n')
        elem = browser.find_element_by_xpath("//*[@id='top_search']")
        elem.clear()
        try:
            if line.find(s) != -1:
                payload.append(line1)
                line = line.replace('/', ',')
                payload.append(line)
                payload.append(s)
                writer.writerow(payload)
                elem.clear()

                continue
            elif line.find(g) != -1:
                payload.append(line1)
                payload.append(line)
                payload.append(g)
                writer.writerow(payload)
                elem.clear()

                continue
            else:
                payload.append(row[0])
                #payload.append("출력:"+line1)
                payload.append("None")
                writer.writerow(payload)
                elem.clear()

                continue
        except:
            browser.quit()


#        try:
#     elem = WebDriverWait(browser, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
# except:
#     browser.quit()
#     print('error')
