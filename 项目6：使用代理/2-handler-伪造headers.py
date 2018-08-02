import urllib.request

httpHandler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(httpHandler)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

request = urllib.request.Request(url='https://www.baidu.com/',headers=headers)

response = opener.open(request)

data = response.read().decode('utf-8')

print(data)