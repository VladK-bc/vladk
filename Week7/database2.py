#!/usr/bin/python3
#VladK database2.py
import csv
import json
import pymysql

## syntax is localhost username, password, database name
db = pymysql.connect(host= 'localhost',
                     user= 'cmdb',
                     password= 'cmdb',
                     database= 'cmdb')

cursor = db.cursor()
sql = "select * device"

try:
    cursor.execute(sql)
    results = cursor.fetchall()

    with open('devicereadout1.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(results)

    with open('devicereadout2.json', 'w') as f:
        json.dump(results, f)

except Exception as e:
    print ("Error", e)

db.close()
s