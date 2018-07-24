import time
import urllib
import urllib.request
import urllib.parse

url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%s&pn=%d'
#kw: 搜索框中的内容
# pn：页数，每页50条内容，0：第一页，50：第二页，100：第三页···
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'Accept-Encoding':'',
}

def start():
    key = input('搜索,输入关键词:')
    key = urllib.parse.quote(key)

    # 让用户输错后可重新输入
    while True:
        try:
            num = int(input("输入爬取多少页:"))
            break
        except Exception as e:
            print('请输入数值型数据!')
    load(key, num)

# 使程序更具有健壮性，当网页返回错误时，会有显示
def load(key, num):
    for i in range(num):
        url_detail = url % (key, i*50)
        print("百度贴吧第%d页,开始下载..." % (i+1))
        try:
            req = urllib.request.Request(url=url_detail, headers=headers)
            res = urllib.request.urlopen(req)
            html = res.read().decode('utf-8')
        except urllib.request.URLError as e:
            print("操作失败:", e.reason)
            html = None
        save(html, i)
        time.sleep(1)

def save(html, i):
    with open('./download/百度贴吧第%d页.html' % (i+1), mode='w', encoding='utf-8') as fw:
        fw.write(html)
        print("百度贴吧第%d页,保存成功！" % (i+1))

if __name__ == '__main__':
    start()