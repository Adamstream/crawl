import urllib.request
import urllib.parse
import json

# 调用手机端翻译，简单
url = 'http://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; MI 6  Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36'
}

# key = input('输入：')
key = '你好'
form = {
    'kw': key
}
form = urllib.parse.urlencode(form).encode('utf-8')
resquest = urllib.request.Request(url=url, headers=headers, data=form)
response = urllib.request.urlopen(resquest)

content = response.read().decode('utf-8')
# print(type(content))
content = json.loads(content)
for i in content['data']:
    print(i['k'])
    print(i['v'])