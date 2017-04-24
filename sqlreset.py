#!/usr/bin/env python

import pymysql

config = {
    'user': 'username',
    'password': 'password',
    'host': 'host',
    'database': 'database'
}

connection = pymysql.connect(**config)
c = connection.cursor()

try:
    with c as cursor:
        sql="delete from yourtable"
        c.execute(sql)
    connection.commit();
finally:
    connection.close()
