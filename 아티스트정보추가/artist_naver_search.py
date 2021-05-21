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
# browser.get(
#     'https://people.search.naver.com/')
with open('fg.csv', 'r',encoding="utf-8-sig") as file:
    csvreader = csv.reader(file)
    # 헤더(컬럼명) 건너뛰고 싶을 때
    #next(csvreader)
    for row in csvreader:
        browser.get(
            "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q="+row[0])
        print('검색:'+row[0])
        payload = []
        elem = browser.find_element_by_xpath('//*[@id="q"]')
        #elem.send_keys(row[0])
        elem.send_keys(Keys.RETURN)
        elem = browser.find_element_by_xpath('//*[@id="q"]')
        html = browser.page_source
        soup = BeautifulSoup(html, "lxml")
        #group = soup.find('div', attrs={'class': 'compo-thumblist ty_size5'})
        group = soup.find('div', {"class": "compo-thumblist ty_size5"})
        #group = soup.find('div', attrs={'data-comp': 'ThumbListItem'})
        if group== -1:
            continue
            # elem.send_keys(Keys.RETURN)
            # browser.get(
            #     "https://people.search.naver.com/")
            # elem = browser.find_element_by_xpath("//*[@id='nx_query']")
            # #print(type(row[0]))
            # print('검색:'+row[0])
            # elem.send_keys(str(row[0]))
            # #elem.submit()
            # elem.send_keys(Keys.RETURN)
            # elem = browser.find_element_by_xpath("//*[@id='nx_query']")
            # html = browser.page_source
            # soup = BeautifulSoup(html, "lxml")
            # group = soup.find(
            #     'span', attrs={'class': 'sub'})
            # elem.clear()
            # if group.get_text == '가수' | group.get_text == '음악인':
            #     browser.find_element_by_xpath("//*[@id='content']/div/div[2]/div[2]/div/div/div/div/a").click()
            #     html = browser.page_source
            #     soup = BeautifulSoup(html, "lxml")
            #     members = soup.findAll('dl', attrs={'class': 'dsc'})
            #     print(type(memebers))
        else:
            payload.append(row[0])
            try:
                for sibling in soup.find('div', {"class": "compo-thumblist ty_size5"}).ul.li.next_siblings:
                    members = sibling.get_text()
                    payload.append(members)
                    print(members+" ")
                    try:
                        pageNumber = soup.find('span', {'class': 'total_page'})
                        nextButton = browser.find_element_by_xpath(
                            '//*[@id="pr0Coll"]/div/div/div/div[1]/div/span[2]/a[2]/span')
                        for i in range(0,pageNumber):
                            if nextButton != -1 and nextButton != None:
                                nextButton.click()
                            for sibling in soup.find('div', {"class": "compo-thumblist ty_size5"}).ul.li.next_siblings:
                                members = sibling.get_text()
                                payload.append(members)
                                print(members+" ")

                    except Exception as e:
                        print(e)
                        browser.quit()
                        continue
                    writer.writerow(payload)
            except Exception as e:
                print(e)
                browser.quit()
                break

                

            # payload.append(row[0])
            # members=group.get_text()
            # payload.append(members)
            # print(members)
            # writer.writerow(payload)
















        
