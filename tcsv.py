import sqlite3

con = sqlite3.connect('ip.db')
cur = con.cursor()
#cur.execute('create table ip(ip char,prot char)')
#cur.execute("insert into ip (ip,prot)values('192.168.1.1','80')")
s = cur.execute("select * from ip")
for i in s:
    print(i)
con.commit()
cur.close()
con.close()
