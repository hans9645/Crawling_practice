#TJ미디어에서 노래방 정보를 받아와서 한국노래의 경우 제목 띄어쓰기 적용 시키는 코드
import requests
import urllib.request
import json
from bs4 import BeautifulSoup
import csv
import re
from pykospacing import spacing

filename = "songs1-12.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)


reg = re.compile(r'[a-zA-Z]')

title = "title\tartist\tcomposer\tlyricist\tdates".split('\t')
writer.writerow(title)
for i in range(0, 21):
    for j in range(1, 13):
        req = requests.get(
            'https://api.manana.kr/karaoke/release/20{}{}/tj.json'.format(str(i).zfill(2), str(j).zfill(2)))
        # if j < 10:
        #     req = requests.get(
        #         'https://api.manana.kr/karaoke/release/20{}0{}/tj.json'.format(str(i).zfill(2), str(j).zfill(2)))
        # else:
        #     req = requests.get(
        #         'https://api.manana.kr/karaoke/release/20{}{}/tj.json'.format(str(i).zfill(2), j))
        datas = req.json()
        results = []
        # title, artist, album, type, release, agency, lyrics, country, composer,lyricist
        
        for data in datas:
            print(type(data))
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
                #print(payload)
                writer.writerow(payload)
            else:
                kospacing_sent = spacing(result['title'])
                payload = [kospacing_sent, result['artist'],
                           result['composer'], result['lyricist'], result['dates']]
                #print(payload)
                writer.writerow(payload)

               






# writer.writerow()
# print(results)

# results[0]['id']="what?"
# print(results[0]['id'])


# for result in results:
#     req = requests.get('https://api.manana.kr/karaoke/release/201901/tj.json')
#     links = req.json()


# for result in results:

#     payload = [result['title'],result['artist'],result['composer'],result['lyricist'],result['dates']]
#     print(payload)
#     writer.writerow(payload)


# for result in results:

#     payload = {
#         "title": result['title'],
#         "artist": result['artist'],
#         "composer": result['composer'],
#         "lyricist": result['lyricist'],
#         "dates": result['dates']
#     }
#     payload = urllib.parse.urlencode(payload)
#     headers = {'content-type': 'application/json'}
#     binary_data = payload.encode('utf-8')

#     r = urllib.request.urlopen(
#         'http://muziker.co.kr/php/New/InsertMusic.php', binary_data)
#     print(r)
