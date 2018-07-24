import json
import urllib.request

# 百度翻译的api接口
url = 'https://fanyi.baidu.com/v2transapi'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Host': 'fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Cookie': 'BIDUPSID=0ACEB5EB33275BA2FFF963104A1ECE1D; PSTM=1529289566; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=F5116FE9BD99F5FE8FE521D2893C3E31:SL=0:NR=10:FG=1; BDUSS=gwYjh4WGRFOGlyRENnTUZEOGJVdlNVbHAzQXJWMVF2cE1jZFRlelpNLVpNVzViQVFBQUFBJCQAAAAAAAAAAAEAAAAmNUVeAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJmkRluZpEZbbD; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22fra%22%2C%22text%22%3A%22%u6CD5%u8BED%22%7D%2C%7B%22value%22%3A%22hu%22%2C%22text%22%3A%22%u5308%u7259%u5229%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1455_21099_26350_22160; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1531487471,1531536123,1532162026,1532423045; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1532423045'
}
key = input('请输入要翻译的内容:')

'''
from	zh
to	en
query	你好
transtype	realtime
simple_means_flag	3
sign	232427.485594
token	b877570f8d8d67dcad7aa657692c7e23
'''
# 构造form表单
form = {
    'from': 'zh',
    'to': 'en',
    'query': key,
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '232427.485594',
    'token': 'b877570f8d8d67dcad7aa657692c7e23'
}

# 对form表单整体进行编码
form = urllib.parse.urlencode(form).encode('utf-8')
resquest = urllib.request.Request(url=url, headers=headers, data=form)
response = urllib.request.urlopen(resquest)

content = response.read().decode('utf-8')
#将Unicode码转化为中文
# content = response.read().decode('unicode-escape')
# print(content)

# 将Unicode码转化为中文，json方式实现
content = json.dumps(json.loads(content, encoding='utf-8'),ensure_ascii=False)
print(content)