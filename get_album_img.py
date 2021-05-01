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
from pykospacing import spacing

sent = '김철수는 극중 두 인격의 사나이 이광수 역을 맡았다. 철수는 한국 유일의 태권도 전승자를 가리는 결전의 날을 앞두고 10년간 함께 훈련한 사형인 유연재(김광수 분)를 찾으러 속세로 내려온 인물이다.'
new_sent = sent.replace(" ", '')  # 띄어쓰기가 없는 문장 임의로 만들기
print(new_sent)
kospacing_sent = spacing(new_sent)
print(sent)
print(kospacing_sent)


with open('songs_adj_jump.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter='\t')
    # 헤더(컬럼명) 건너뛰고 싶을 때
    next(csvreader)
    for row in csvreader:
        print(row)
