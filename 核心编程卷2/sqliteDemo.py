import sqlite3

cx = sqlite3.connect("E:/test.db")
cu = cx.cursor()

# cu.execute("create table catalog(id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")

# for t in [(0,10,'abc','YU'), (1,20,'cba','Xu')]:
# 	cu.execute("insert into catalog values (?,?,?,?)",t)

# cx.commit()


cu.execute("update catalog set name='Boy' where id = 0")
cx.commit()

# cu.execute("delete from catalog where id = 1")
# cx.commit()

cu.execute("select * from catalog")
for t in cu.fetchall():
	print t

help(sqlite3)