import sqlite3
import requests

con = sqlite3.connect('./ip.db')
cur = con.cursor()
ip = cur.execute("select ip from ip")
for i in ip:
    #print(i[0])
    proxies = {"http":i[0]}
    try:
        t = requests.get("http://www.baidu.com", proxies=proxies, timeout=5)
        if t.status_code == 200:
            print("可用",i)
        else:
            print("无效", i)
    except:
        print("失败", i)
