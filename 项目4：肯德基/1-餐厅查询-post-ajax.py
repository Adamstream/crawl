import urllib.request
import urllib.parse

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

url_get = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid&cname=&pid=13&pageIndex=1&pageSize=10'
cityName = input('输入城市')
pageIndex = int(input('选取页数'))
pageSize = int(input('每页餐厅数'))
'''
form = {
    'cname': cityName,
    'pid': serviceType,
    'pageIndex': pageIndex,
    'pageSize': pageSize
}
'''

'''
serviceType
全天营业:13
生日餐会:20
Wi - Fi:31
店内参观:21
三对三:19
手机点餐:35
'''


if __name__ == "__main__":
    for page in range(1,pageIndex+1):
        while True:
            print('################################################')
            print('                  全天营业:13')
            print('                  生日餐会:20')
            print('                  Wi - Fi:31')
            print('                  店内参观:21')
            print('                  三对三:19')
            print('                  手机点餐:35')
            print('################################################')
            try:
                serviceType = int(input('选取服务类型:'))
                if not serviceType==13 or serviceType==20 or serviceType==31 or serviceType==21 or serviceType==19 or serviceType==35:
                    raise()
                break
            except:
                print('选择有误,重新选择!')
        form = {
            'cname': cityName,
            'pid': serviceType,
            'pageIndex': page,
            'pageSize': pageSize
        }
        form = urllib.parse.urlencode(form).encode('utf-8')
        request = urllib.request.Request(url=url, data=form, headers=headers)
        response = urllib.request.urlopen(request)
        data = response.read().decode('utf-8')
        with open('./download/肯德基%d.json' % page, mode='wb') as fw:
            fw.write(data.encode('utf-8'))