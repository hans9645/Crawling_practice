import requests
import urllib.request
import json
from bs4 import BeautifulSoup
import csv
import re
import selenium

filename = "tags.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)


reg = re.compile(r'[a-zA-Z]')

title = "title\tartist\tcomposer\tlyricist\tdates".split('\t')
writer.writerow(title)
for i in range(19, 21):
    for j in range(1, 13):
        if j < 10:
            req = requests.get(
                'https://api.manana.kr/karaoke/release/20{}0{}/tj.json'.format(i, j))
        else:
            req = requests.get(
                'https://api.manana.kr/karaoke/release/2020{}/tj.json'.format(i, j))
        datas = req.json()
        results = []
        # title, artist, album, type, release, agency, lyrics, country, composer,lyricist

        for data in datas:
            results.append({
                'id': None,
                'title': data['title'],
                'artist': data['singer'],
                'composer': data['composer'],
                'lyricist': data['lyricist'],
                'album': '',
                'lyrics': '',
                'type': '',
                'dates': data['release'],
                'country': '',
                'link': ''
            })

        for result in results:
            if reg.match(result['title']) and reg.match(result['artist']) and reg.match(result['composer']) and reg.match(result['lyricist']):
                payload = [result['title'], result['artist'],
                           result['composer'], result['lyricist'], result['dates']]
                # print(payload)
                # writer.writerow(payload)
                requestpost = requests.post("http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=0a4980a82d68920e6069a9ce4ab33bd3&artist={}&track={}&format=json".format(
                    payload[1], payload[0]))
                response_data = requestpost.json()
                try:
                    tags=[]
                    for data in response_data["track"]["toptags"]['tag']:
                        print(data['name'])
                        tags.append(data['name'])
                    rr = [payload[1], payload[0], tags]
                    writer.writerow(rr)
                except:
                    continue


# requestpost = requests.post("http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=0a4980a82d68920e6069a9ce4ab33bd3&artist={}&track={}&format=json".format(
#     str(payload['artist']), str(payload['title'])))
# response_data = requestpost.json()
# for data in response_data["track"]["toptags"]['tag']:
#     print(data['name'])

