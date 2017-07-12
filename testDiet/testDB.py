#!/usr/bin/env python
import pymysql
conn = pymysql.connect(host='dietopteam1.cotfgzkq3gdm.us-west-2.rds.amazonaws.com', port=3306, user='dietopteam', passwd='welcometodiet', db='dietop', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        sql = "SELECT * FROM `food` WHERE `foodname`=%s"
        cursor.execute(sql, ('Apple',))
        result = cursor.fetchone()
        print(result)
finally:
    conn.close()

