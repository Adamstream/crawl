import urllib.request
import re
import json

# 开始爬取,只能爬取首页
url = 'http://www.xicidaili.com/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'Accept-Encoding':'',
}
pattern = r'<td>([\d\.]+?)</td>.*?\n.*?<td>([\d]+?)</td>'
pattern = r'<td>([\d\.]+?)</td>.*\n.*'
pattern += r'<td>([\d]+?)</td>.*\n.*'
pattern += r'<td>([\w]+?)</td>.*\n.*'
pattern += r'<td class="country">([\w]+?)</td>.*\n.*'
pattern += r'<td>([\w]+?)</td>'
def load(url,headers,pattern):
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    data = res.read().decode('utf-8')
    p = re.compile(pattern=pattern)
    pData = re.findall(pattern=p, string=data)
    save(pData)

def save(pData):
    title = ['IP地址', '端口', '服务器地址', '是否匿名', '类型']
    listData = []
    dictData = {}
    for i in pData:
        dictData[title[0]] = i[0]
        dictData[title[1]] = i[1]
        dictData[title[2]] = i[2]
        dictData[title[3]] = i[3]
        dictData[title[4]] = i[4]
        listData.append(dictData)
    with open('2-re-西刺代理-爬取首页-data.json', mode='w', encoding='utf-8') as f:
        json.dump(listData, f, ensure_ascii=False)

if __name__=='__main__':
    load(url,headers,pattern)