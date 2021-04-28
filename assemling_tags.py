import requests
import urllib.request
import json
from bs4 import BeautifulSoup
import csv
import re
import selenium
import time

filename = "tags.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)


with open('songs_adj_jump.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter='\t')
    # 헤더(컬럼명) 건너뛰고 싶을 때
    next(csvreader)
    for result in csvreader:
        r_result=result[0].split(',')
        # print(rr[0])
        payload = [r_result[0], r_result[1],
                   r_result[2], r_result[3], r_result[4]]
         # print(payload)
         # writer.writerow(payload)

        try:
            requestpost = requests.post("http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=&artist={}&track={}&format=json".format(payload[1], payload[0]))
            response_data = requestpost.json()
            try:
                tags = []
                for data in response_data["track"]["toptags"]['tag']:
                    print(data['name'])
                    tags.append(data['name'])
                rr = [payload[1], payload[0], tags]
                writer.writerow(rr)
            except:
                #time.sleep(0.001)
                print('[]')
                continue
        except:
            time.sleep(5)
            requestpost = requests.post(
                "http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=&artist={}&track={}&format=json".format(payload[1], payload[0]))
            response_data = requestpost.json()
            try:
                tags = []
                for data in response_data["track"]["toptags"]['tag']:
                    print(data['name'])
                    tags.append(data['name'])
                rr = [payload[1], payload[0], tags]
                writer.writerow(rr)
            except:
                #time.sleep(0.001)
                print('[]')
                continue






    


