import requests,re
from bs4 import BeautifulSoup
url = 'http://m.58.com/lanshanqu/ershoufang/pn{}/?58ihm=m_house_index_ershoufang&58cid=505&PGTID=0d30000c-001f-9c02-2a1a-33501b2fecdb&ClickID=3&segment=true'
headers = {
'Host': 'm.58.com',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Linux; Android 4.3; Nexus 10 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'DNT': '1',
'Accept-Encoding': 'gzip, deflate, sdch',
'Accept-Language': 'zh-CN,zh;q=0.8',
}
r = r'"http://m.58.com/linyi/ershoufang/\d+x.shtml'
rs = requests.session()
with open('./58id.txt', 'a') as f:
    for i in range(1,71):
        t = rs.get(url.format(i), headers=headers).text
        shtml = re.findall(r,t)
        for id in shtml:
            f.write(id+'\n')