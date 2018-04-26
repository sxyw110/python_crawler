#coding:utf-8
__author__ = 'liukoo'
import urllib, urllib.request,cookiejar,re
from hashlib import md5
class LoginAlimama:
    def __init__(self):
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36'}
        #cookie 支持
        self.cookie_handle =  cookiejar.CookieJar();
        self.opener =  urllib.request.build_opener( urllib.request.HTTPCookieProcessor(self.cookie_handle))
        urllib.request.install_opener(self.opener)
    #登陆
    def login(username,passwd):
        login_data = {
            'logname':'',
            'originalLogpasswd':'',
            'logpasswd':'',
            'proxy':'',
            'redirect':'',
            'style':''
        }
        login_data['logname'] =username
        login_data['originalLogpasswd'] =passwd
        login_data['logpasswd'] = md5(login_data['originalLogpasswd']).hexdigest()
        source =  urllib.request.urlopen('http://www.alimama.com/member/minilogin.htm').read()
        token_list = re.findall(r"input name='_tb_token_' type='hidden' value='([a-zA-Z0-9]+)'", source)
        login_data['_tb_token_'] = token_list[0] if token_list else ''
        loginurl = 'https://www.alimama.com/member/minilogin_act.htm'
        #拼接post数据
        login_data = urllib.urlencode(login_data)
        self.header['Referer'] = 'http://www.alimama.com/member/minilogin.htm'
        try:
            req =  urllib.request.Request(url=loginurl,data=login_data,headers=self.header)
            resp = urllib.request.urlopen(req)
            html = resp.read()
            if str(resp.url).find('success')!=-1:
                return True
        except Exception as err:
            print(err);

    if __name__ == '__main__':
        result = login("sxyw110","7236570tb");
        print(result);