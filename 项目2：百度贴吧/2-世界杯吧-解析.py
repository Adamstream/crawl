import urllib
import urllib.request
import urllib.parse
import re

url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%s&pn=%d'
#kw: 搜索框中的内容
# pn：页数，每页50条内容，0：第一页，50：第二页，100：第三页···
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'Accept-Encoding':'',
}

def start():
    key = input('搜索,输入关键词:')
    # key = '世界杯'
    key = urllib.parse.quote(key)
    # print(key)

    # 让用户输错后可重新输入
    while True:
        try:
            num = int(input("输入爬取多少页:"))
            break
        except Exception as e:
            print('请输入数值型数据!')

    load(url, key, num, headers)
    # html = load(url, key, num, headers)
    # print(html)
    # save(html)
    # parse(html)

# 使程序更具有健壮性，当网页返回错误时，会有显示
def load(url, key, num, headers):
    for i in range(num):
        url_detail = url % (key, i*50)
        try:
            req = urllib.request.Request(url=url_detail, headers=headers)
            res = urllib.request.urlopen(req)
            html = res.read().decode('utf-8')
        except urllib.request.URLError as e:
            print("操作失败:", e.reason)
            html = None
        save(html, i)

def save(html, i):
    with open('./download/百度贴吧第%d页.html' % i, mode='w', encoding='utf-8') as fw:
        fw.write(html)
        print("百度贴吧第%d页,保存成功！" % i)

def parse(html):
    # pattern = r'<dt.*?"([\d]+?)个回复".*?title="(.*?)">.*?un=(.*?)&.*?</dt>'
    pattern = r'<ul id="thread_top_list".*?title="回复">([\d]+)</span>.*?<a rel="noreferrer" href="/p/5781082958" title="(.*?)".*?title="主题作者: (.*?)".*?</li>'
    p = re.compile(pattern, re.S)
    pData = re.findall(pattern=p, string=html)
    print(pData)


if __name__ == '__main__':
    start()