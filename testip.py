import sqlite3,time
import requests
import queue
from threading import Thread

con = sqlite3.connect('./ip.db')
cur = con.cursor()
ip = cur.execute("select ip from ip")
uip = queue.Queue()
q = queue.Queue()
for i in ip:
    q.put(i[0])
def testip(q, uip):
    while True:
        if q.empty():
            break
        else:
            ip = q.get()
            proxies = {"http":ip}
            try:
                t = requests.get("http://ip.chinaz.com/", proxies=proxies, timeout=5)
                if t.status_code == 200:
                    print("可用",ip)
                else:
                    print("无效", ip)
            except:
                print('失败', ip)
                uip.put(ip)
    return uip
for i in range(5):
    t = Thread(target=testip, args=(q,uip))
    t.start()
t.join()
time.sleep(3)
def duip(uip):
    while True:
        if uip.empty():
            break
        else:
            cur.execute("delete from ip where ip = '{}'".format(uip.get()))
con.commit()

nip = cur.execute("select ip from ip")
for i in nip:
    print(i[0])
cur.close()
con.close()
