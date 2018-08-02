import urllib.request

httpHandler = urllib.request.HTTPHandler()

opener = urllib.request.build_opener(httpHandler)

urllib.request.install_opener(opener)

# response = urllib.request.urlopen(url='https://www.baidu.com/')
response = urllib.request.urlopen(url='http://www.baidu.com/')

data = response.read().decode('utf-8')

print(data)