#!user/bin/env python
# -* - coding: UTF-8 -* - 

import os, sys
import MySQLdb
try:
    conn MySQLdb.connect(host=’localhost’,user=’root’,passwd=’’,db=’address’
except Exception,e:
    print e
    sys.exit()
cursor=conn.cursor()
sql=’insert into address(name, address) values(%s, %s)’
value=((“zhangsan”,”haidian”),(“lisi”,”haidian”))
try
    cursor.executemany(sql,values)
except Exception, e:
    print e
sql=”select * from address”
cursor.execute(sql)
data=cursor.fetchall()
if data
    for x in data:
        print x[0],x[1]
cursor.close()
conn.close()