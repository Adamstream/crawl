import urllib.request

url = 'https://www.douban.com/people/160339492/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
data = response.read().decode('utf-8')

with open('./download/无cookie数据.html',mode='w',encoding='utf-8') as fw:
    fw.write(data)