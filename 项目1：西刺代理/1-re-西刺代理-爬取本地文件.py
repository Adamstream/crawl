import re
import json

'''
<tr class="odd">
    <td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>
    <td>222.185.22.253</td>
    <td>6666</td>
    <td>江苏常州</td>
    <td class="country">高匿</td>
    <td>HTTPS</td>
      <td>41天</td>
    <td>2分钟前</td>
  </tr>
  
  <tr class="">
    <td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>
    <td>125.120.9.120</td>
    <td>808</td>
    <td>浙江杭州</td>
    <td class="country">高匿</td>
    <td>HTTP</td>
      <td>486天</td>
    <td>3分钟前</td>
  </tr>
'''

# 测试
def save(pData):
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
    with open('1-re-西刺代理-爬取本地文件-data.json', mode='w', encoding='utf-8') as f:
        json.dump(listData, f, ensure_ascii=False)

with open('./1-西刺代理-首页.html', mode='r', encoding='utf-8') as fr:
    rData = fr.read()
    pattern = r'<td>([\d\.]+?)</td>.*\n.*'
    pattern += r'<td>([\d]+?)</td>.*\n.*'
    pattern += r'<td>([\w]+?)</td>.*\n.*'
    pattern += r'<td class="country">([\w]+?)</td>.*\n.*'
    pattern += r'<td>([\w]+?)</td>'
    p = re.compile(pattern=pattern)
    pData = re.findall(pattern=p, string=rData)
    save(pData)