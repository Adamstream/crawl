import urllib.request
import urllib.parse
from http.cookiejar import CookieJar

# 使用CookieJar保存cookie

url = 'https://accounts.douban.com/login'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
form = {
    'source':None,
    'redir':'https://www.douban.com',
    'form_email':'手机或邮箱',
    'form_password':'密码',
    'login':'登录'
}
form = urllib.parse.urlencode(form).encode('utf-8')

# post登陆，保存cookie
cookiejar = CookieJar()

cookieHandler = urllib.request.HTTPCookieProcessor(cookiejar=cookiejar)

opener = urllib.request.build_opener(cookieHandler)

urllib.request.install_opener(opener)

# 第一步，登陆

request = urllib.request.Request(url=url,headers=headers,data=form)

urllib.request.urlopen(request)

print('#####################登陆成功————————————')


# 第二步，获取个人主页
url_person = 'https://www.douban.com/people/160339492/'

request = urllib.request.Request(url=url_person,headers=headers)

response = urllib.request.urlopen(request)

data = response.read().decode('utf-8')

print(data)