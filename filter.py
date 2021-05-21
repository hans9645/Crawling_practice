import csv


filename = "fg.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

search_keyword = 0
artists = set()
with open('csv-Files/result.csv', 'r') as f:
    csvreader = csv.reader(f, delimiter=',')
    # 헤더(컬럼명) 건너뛰고 싶을 때
    next(csvreader)
    for row in csvreader:
        # print(row[0])
        word1=row[0]
        word2=row[1]
        locate = row[0].find('(')
        payload=[]
        if locate !=-1:
            word1=word1[:locate]
        if word2=='그룹':
            payload.append(word1)   
            payload.append(word2)
            writer.writerow(payload)
