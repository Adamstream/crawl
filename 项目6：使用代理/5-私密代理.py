import urllib.request


proxies = {
    'http':'用户名:密码@ip:端口'
}

proxyHandler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(proxyHandler)

response = opener.open(fullurl='http://www.baidu.com/')

data = response.read().decode('utf-8')

print(data)