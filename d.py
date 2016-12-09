#!/usr/bin/python3
import requests, re
import queue, time
import random, sqlite3
from bs4 import BeautifulSoup
from threading import Thread
from requests import exceptions
con = sqlite3.connect('./ip.db')
cur = con.cursor()
cur.execute("create table ip (id integer primary key autoincrement,ip char)")
q = queue.Queue()
o = queue.Queue()
def cip():#提取代理
    ipre = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}' #IP正则
    po1 = r'<td>\d{2,4}</td>' #端口正则
    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko)    Chrome/48.0.2564.23 Mobile Safari/537.36"} #伪造HEAD
    for i in range(5):
        t = requests.get("http://www.xicidaili.com/nn/{}".format(str(i+1)), headers=headers).content.decode("utf-8")
    #print(t)
        soup = BeautifulSoup(t,"lxml")
        s = soup.find_all("tr")
        for i in s:
            o = re.findall(ipre, str(i))
            po = re.findall(po1,str(i))
            with open("./ip.txt",'a') as f:
                for (p,pot) in zip(o,po):
                    f.write(p+":"+pot.replace("<td>","").replace("</td>","")+'\n')



def read_ip(): #读取代理返回队列
    with open("./ip.txt", 'r') as f:
        ips = f.readlines()
    for i in ips:
        q.put("http://"+i.strip())
    return q

def test_ip(q,o):
    pn = 1
    url = "http://www.baidu.com"
    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko)    Chrome/48.0.2564.23 Mobile Safari/537.36"} #伪造HEAD
    while True:
        if q.empty():
            break
        else:
            h = q.get()
            proxies = {"http":h}
            try:
                t = requests.get(url, headers=headers, proxies=proxies, timeout=10)
                print(t.status_code)
                if t.status_code==200:
                    o.put(h)
            except:
                pass

cip()

read_ip()
for i in range(200):
    t1 = Thread(target=test_ip, args=(q,o))
    t1.start()
t1.join()
time.sleep(2)
while True:
    if o.empty():
        break
    else:
        cur.execute("insert into ip (ip)values('{}')".format(o.get()))

con.commit()
cur.close()
con.close()
