import urllib.request

httpHandler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(httpHandler)

response = opener.open(fullurl='http://www.baidu.com/')

data = response.read().decode('utf-8')

print(data)
