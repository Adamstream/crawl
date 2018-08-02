import urllib.request

proxies = {
    'http': '116.62.194.248:3128'
}

proxyHandler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(proxyHandler)

response = opener.open(fullurl='http://www.baidu.com/')

data = response.read().decode('utf-8')

print(data)