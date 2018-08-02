import urllib.request

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

proxies = {
    'https':'124.235.208.252:443'
}

proxyHandler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(proxyHandler)

response = opener.open(request)

data = response.read().decode('utf-8')

print(data)