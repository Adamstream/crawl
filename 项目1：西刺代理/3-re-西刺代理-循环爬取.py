import time
import urllib
import urllib.request
import re
import json

# 循环爬取并保存在文件中,只爬取每种代理的100页

url_base = 'http://www.xicidaili.com/'
url_suf = ['nn/', 'nt/', 'wn/', 'wt/']
url_name = ['国内高匿代理', '国内普通代理', '国内HTTPS代理', '国内HTTP代理']
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

def save(pData, str, n):
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
    with open('3-re-西刺代理-循环爬取-data-%s-%d.json'%(str,n), mode='a+', encoding='utf-8') as f:
        json.dump(listData, f, ensure_ascii=False)

def load(url,headers,pattern,str,n):
    req = urllib.request.Request(url=url, headers=headers)
    res = urllib.request.urlopen(req)
    data = res.read().decode('utf-8')
    pattern = r'<td>([\d\.]+?)</td>.*?'
    pattern += r'<td>([\d]+?)</td>.*?'
    pattern += r'<td>([\w]+?)</td>.*?'
    pattern += r'<td class="country">([\w]+?)</td>.*?'
    pattern += r'<td>([\w]+?)</td>'
    p = re.compile(pattern, re.S)
    pData = re.findall(pattern=p, string=data)
    save(pData,str,n)

def start():
    for i in range(4):
        for j in range(100):
            url = url_base + url_suf[i] + str(j+1)
            print(url)
            load(url,headers,pattern,url_name[i],j)
            time.sleep(1)
if __name__ == '__main__':
    start()