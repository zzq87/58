#!/usr/bin/python3
import requests, re
from bs4 import BeautifulSoup
pro = {"http":"124.88.67.20:80"}
s = requests.get("http://ip.chinaz.com", proxies=pro).text
soup  = BeautifulSoup(s, "lxml")
ip = soup.find_all(class_="fz24")
for i in ip:
    print(re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(i))[0])
