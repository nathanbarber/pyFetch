#!/usr/bin/env python

import pymysql
import json
import os

config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_hostname',
    'database': 'your_mysql_database'
}
def dataquery(toggle):
    connection = pymysql.connect(**config)
    c = connection.cursor()
    try:
        with c as cursor:
            sql = "SELECT * FROM your_table"
            c.execute(sql)
            result = c.fetchall()
            for item in result:
                print str(item[0]) + " - {"
                d = json.loads(item[1])
                for i in d:
                    print "'" + d[i] + "'"
                print "}\n"
            if toggle:
                for item in result:
                    f = open(os.path.expanduser("your_path_to_copy_file") + str(item[0]) + ".txt", "w+");
                    f.write("{ \n")
                    d = json.loads(item[1])
                    for i in d:
                        if i == "specify":
                            f.write("\n")
                            f.write("" + d[i] + "\n")
                            f.write("\n")
                        else:
                            f.write("  " + d[i] + "\n")
                            
                    f.write("}\n")

    finally: 
        connection.close()
dataquery(True)
