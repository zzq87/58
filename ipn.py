#!/usr/bin/python3
import requests
pro = {"http":"124.88.67.20:80"}
s = requests.get("http://ip.chinaz.com", proxies=pro).text
print(s)
