import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class RequestsTest(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
            'Referer': 'https://passport.weibo.cn/signin/login?entry=mweibo&r=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=',
        }
        self.session=requests.session()
        self.loginurl='https://passport.weibo.cn/sso/login'

    #登录
    def login_weibo(self,username,password):
        data={
            'username': username,
            'password': password,
            'savestate': '1',
            'r': '',
            'ec': '0',
            'pagerefer': 'http://weibo.cn/',
            'entry': 'mweibo',
            'wentry': '',
            'loginfrom': '',
            'client_id': '',
            'code': '',
            'qq': '',
            'mainpageflag': '1',
            'hff': '',
            'hfp': '',
        }
        r = self.session.post(url=self.loginurl,data=data,headers=self.headers)
        print(r)
        #return self.session
        return self.session.cookies

    #普通requests请求不能获取登录后的信息
    def get_info(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',}
        r = requests.get(url=url,headers=headers)
        r.encoding='gbk'
        # print(self.url)
        print(r.text)

    #通过session可以获取登录后的信息
    def session_get_info(self,url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', }
        r = self.session.get(url=url,headers=self.headers)
        print(r.text)

#post_url = 'https://passport.weibo.cn/sso/login'
#get_url = 'https://weibo.cn/6388179289/info'

#实例化微博访问
#weibo_request = RequestsTest().login_weibo('wangzheng@nicetv.com.cn','tcwz1234')

#登录，参数为登录post地址
if __name__ == "__main__":
    RequestsTest().login_weibo('wangzheng@nicetv.com.cn','tcwz1234')
#获取用户详情
#weibo_request.session_get_info(get_url)
