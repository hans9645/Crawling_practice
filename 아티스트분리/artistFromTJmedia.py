#TJ미디어에서 노래방 정보를 받아와서 SET에 그룹, feat, prod,솔로 다 분리시켜서 담는코드
import requests
import urllib.request
import json
from bs4 import BeautifulSoup
import csv
import re
from pykospacing import spacing

filename = "singer_name.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

artists = set()
reg = re.compile(r'[a-zA-Z]')

title = "artist".split('\t')
writer.writerow(title)

for i in range(10, 22):
    for j in range(1, 13):
        if i==21:
            if j>4:
                continue
        # if i < 10:
        #     a=i
        #     a=format(a,'02')
        if j < 10:
            req = requests.get(
                'https://api.manana.kr/karaoke/release/20{}0{}/tj.json'.format(i, j))
        else:
            req = requests.get(
                'https://api.manana.kr/karaoke/release/20{}{}/tj.json'.format(i, j))
        datas = req.json()

        for data in datas:
            # print(type(data['singer']))
            text=data['singer']
            text = text.replace('"', '').replace(')', '').replace(
                '×', ',').replace('Prod.', ',').replace('Feat.', ',').replace(r' of ', ',').replace('(', ',').replace('*', ',').replace('With ', ',').replace('Song By ', ',').replace('Piano by ', ',').replace('&', ',').replace(' By ', ',').replace(' by ',',')
            #print(text)
            flag=1
            while flag:
                locate = text.find(',')
                if locate >= 1:
                    artist = text[:locate]
                    artist.replace('"', '')
                    artist.replace(',', '')
                    artists.add(artist)
                    text = text[locate:]
                elif locate==0:
                    text=text.lstrip(',')
                else:
                    text.rstrip(',')
                    flag=0
                    artists.add(text)


for i in artists:
    print(i)
    payload = [i]
    payload[0].replace(',','')
    #print(payload)
    writer.writerow(payload)
            

