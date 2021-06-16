import re
import pandas as pd
import csv
from sqlalchemy import create_engine, text

db = {
    'user': 'arcane',
    'passwd': 'Arcane123',
    'database': 'arcanedb',
    'charset': 'utf8-sig',
    'host': 'arcanedb.cyu9nbnbjetu.ap-northeast-2.rds.amazonaws.com',
    'port': 3306
}

db_url = f"mysql+mysqlconnector://{db['user']}:{db['passwd']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"


def conn_mysqldb():
    db_conn = create_engine(db_url, encoding='utf-8', max_overflow=0)
    db_conn.connect()
    return db_conn

# 정규식을 이용하여 텍스트의 괄호와 괄호 안 문자열 제거
regex = "\(.*\)|\s-\s.*"
text = "오늘은 딸기(서향딸기, 600g, 1팩 당 5,000원)가 좋습니다!"

#print(re.sub(regex, '', text))  # 오늘은 딸기가 좋습니다!
mysql_db = conn_mysqldb()
with open('target.csv', 'r') as f:
    csvreader = csv.reader(f)
    # 헤더(컬럼명) 건너뛰고 싶을 때
    next(csvreader)
    for row in csvreader:
        artist_name=row[0]
        # isexist = mysql_db.execute("SELECT id FROM artist WHERE name='%s' "%str(artist_name)).fetch()
        # if isexist!=None:
        command = "INSERT INTO artist_new(name) VALUES(%s)"
        mysql_db.execute(command,artist_name)
        members=re.sub(regex, '', row[1])
        artist_members=members.split(',')
        command = "SELECT id FROM artist_new WHERE name = %s LIMIT 1 "
        group_id=mysql_db.execute(command, artist_name).fetchone()
        for member in artist_members:
            line = "INSERT INTO artist_new(name) VALUES (%s)"
            mysql_db.execute(line,member)
            line2 = "SELECT id FROM artist_new WHERE name = %s LIMIT 1 "
            artist_id = mysql_db.execute(line2, member).fetchone()
            # artist_id = mysql_db.execute(
            #     "SELECT id FROM artist_new WHERE name = '%s' LIMIT 1 " % str(member)).fetchone()
            print(member)
            print(group_id[0])
            command2 = "INSERT INTO group_artist_new(group_id,artist_id)  VALUES(%s,%s) "
            mysql_db.execute(command2,(group_id[0], artist_id[0]))




