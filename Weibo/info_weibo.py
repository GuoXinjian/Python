#!/usr/bin/env python3
#coding=utf-8
#test
import requests
import time
import pymysql
from multiprocessing import Pool
from bs4 import BeautifulSoup
import os, random
from login import RequestsTest

def get_ip_list(url,header):
    j=1
    ip_list = []
    while j<2:
        web_data = requests.get(url+str(j),headers=header,timeout=1)
        #print(web_data.content)
        soup = BeautifulSoup(web_data.text, 'lxml')
        #print(soup)
        ips = soup.find_all('tr')
        
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[5].text + '://' + tds[1].text + ':' + tds[2].text)
        j+=1
        #检测ip可用性，移除不可用ip：（这里其实总会出问题，你移除的ip可能只是暂时不能用，剩下的ip使用一次后可能之后也未必能用）
    print(len(ip_list))
    for ip in ip_list:
        print(ip)
        try:
            if ip[:7]=='HTTP://':
                proxy_temp = {'http' : ip}
            else:
                proxy_temp = {'https' : ip}
            res = requests.get('http://www.baidu.com', proxies=proxy_temp,timeout=3)
        except Exception as e:
            ip_list.remove(ip)
            continue
    print(len(ip_list))
    return ip_list

def get_random_ip(proxy_ip):
    if proxy_ip[:7]=='HTTP://':
        proxies = {'http': proxy_ip}
    else:
        proxies = {'https': proxy_ip}
    return proxies


class User_Weibo():#一个实例=一个账号

    def __init__(self,userid=None,proxy=None,cookies=None,headers=None,**userdata):    #type(userdata)==json,如果传入data，则不再发起请求
        self.id=userid
        self.screen_name=None
        self.profile_image_url=None
        self.avatar_hd=None
        self.statuses_count=None
        self.verified=None
        self.verified_type=None
        self.verified_reason=None
        self.close_blue_v=None
        self.description=None
        self.gender=None
        self.mbtype=None
        self.urank=None
        self.mbrank=None
        self.followers_count=None
        self.follow_count=None
        self.data=None
        if userdata:
            self.data=userdata['userdata']
            keys=self.__dict__#如果存在data，将data转为类属性
            for k,v in self.data.items():
                keys[k]=v
        elif type(self.id).__name__!='int':
            print('错误：请输入用户数字id')
            return
        else:
            self.id=userid
            print('查询用户数据......')
            self.apiurl='https://m.weibo.cn/api/container/getIndex?containerid=100505'+str(self.id)
            self.response=requests.get(self.apiurl,proxies=proxy,cookies=cookies,headers=headers,timeout=3)
            if self.response.status_code==403:
                print('403：服务器拒绝访问')
            elif self.response.status_code==503:
                print('503：访问过快')
            elif self.response.text[:15]=='<!doctype html>':
                print('需登录')
            else:
                self.res=self.response.json()
                self.valid=self.res['ok']
                if self.valid==0:
                    print(userid,':查无此人')
                else:
                    print('成功')
                    self.data=self.res['data']['userInfo'] 
                    keys=self.__dict__
                    for k,v in self.data.items():
                        keys[k]=v
        
    @staticmethod
    def getUserInfo(userid=None,proxy=None,cookies=None,headers=None):
        if type(userid).__name__!='int':
            print('错误：请输入用户数字id')
            return
        else:
            userid=userid
            print('查询用户数据......')
            apiurl='https://m.weibo.cn/api/container/getIndex?containerid=100505'+str(userid)
            response=requests.get(apiurl,proxies=proxy,cookies=cookies,headers=headers,timeout=3)
            if response.status_code==403:
                print('403：服务器拒绝访问')
            elif response.status_code==503:
                print('503：访问过快')
            elif response.text[:15]=='<!doctype html>':
                print('需登录')
            else:
                res=response.json()
                valid=res['ok']
                if valid==0:
                    print(userid,':查无此人')
                else:
                    print('成功')
                    data=res['data']['userInfo']             
        return data

class StatusesByUser_Weibo():#每一个实例为1个账户的微博
    def __init__(self,userid):
        if type(userid).__name__!='int':
            print('错误：请输入用户数字id')
            return
        self.userid=userid
        self.statusesdataAll=[]
        self.statusids=[]
    def getStatuses(self,numberlimit=50,laststatusid=0,lasttime=0,proxy=None,cookies=None,headers=None):
        #时间限制还没写
        self.statusesdata=[]
        self.number=0
        self.numberlimit=numberlimit
        self.laststatusid=laststatusid
        self.lasttime=lasttime
        if type(laststatusid).__name__!='int':
            print('请输入微博数字id')
            return
        elif lasttime!=0 and (type(lasttime).__name__!='int' or len(lasttime)!=8):
            print('请输入8位数字日期:YYYYMMdd')
            return
        else:
            if len(self.statusesdataAll)==0:
                print('获取%d条微博'%self.numberlimit)
            else:
                print('再获取%d条微博'%self.numberlimit)
            self.page=0
            self.timeNow=int(time.strftime("%Y%m%d", time.localtime()))       
            while self.number<self.numberlimit:
                self.apiurl='https://m.weibo.cn/api/container/getIndex?containerid=107603'+str(self.userid)+'&page='+str(self.page)
                self.response=requests.get(self.apiurl,proxies=proxy,cookies=cookies,headers=headers,timeout=3)
                if self.response.status_code=='403':
                    print('403：服务器拒绝访问')
                    break
                elif self.response.status_code=='503':
                    print('503：访问过快')
                    break
                elif self.response.text[:15]=='<!doctype html>':
                    print('需登录')
                    break
                else:
                    self.res=self.response.json()
                    if self.res['ok']==0:
                        print('没有更多的微博了')
                        break
                    else:
                        print('成功')
                        self.cards=self.res['data']['cards']
                        for card in self.cards:
                            if card['card_type']==9 and self.number<self.numberlimit:
                                if int(card['mblog']['id'])>=self.laststatusid and card['mblog']['id'] not in self.statusids:
                                    self.statusesdata.append(card['mblog'])
                                    self.statusids.append(card['mblog']['id'])
                                    self.number+=1
                time.sleep(2)
                self.page+=1
            self.statusesdataAll.extend(self.statusesdata)
            return self.statusesdata

class StatusesByTopic_Weibo():#每一个实例为1个话题下的微博                    
    def __init__(self,topic):
        self.topic=topic

class Status_Weibo():#单条微博实例
    def __init__(self,statusid=None,proxy=None,cookies=None,headers=None,**statusdata):
        self.id=statusid
        self.statusdata=None
        self.bid=None
        self.can_edit=None
        self.comments_count=None
        self.content_auth=None
        self.created_at=None
        self.isLongText=None
        self.is_paid=None
        self.mblog_vip_type=None
        self.mblogtype=None
        self.mid=None
        self.more_info_type=None
        self.pending_approval_count=None
        self.attitudes_count=None
        self.reposts_count=None
        self.source=None
        self.text=None
        self.user=None
        self.obj_ext=None
        if statusdata:
            self.statusdata=statusdata['statusdata']
            keys=self.__dict__
            for k,v in self.statusdata.items():
                keys[k]=v
        elif self.id==None:
            print('请输入单条微博id或单条微博数据')
            return
        else:
            print('查询微博数据......')
            self.apiurl='https://m.weibo.cn/statuses/show?id='+str(self.id)
            self.response=requests.get(self.apiurl,proxies=proxy,cookies=cookies,headers=headers,timeout=3)
            if self.response.status_code==403:
                print('403：服务器拒绝访问')  
            elif self.response.status_code==503:
                print('503：访问过快')
            elif self.response.text[:15]=='<!doctype html>':
                print('需登录')
            else:
                self.res=self.response.json()
                self.valid=self.res['ok']
                if self.valid==0:
                    print(self.id,':未查到')
                else:
                    print('成功')
                    self.statusdata=self.res['data']
                    keys=self.__dict__
                    for k,v in self.statusdata.items():
                        keys[k]=v

class Hot_Weibo():
    def __init__(self,page=50):
        self.page=0
        self.data=[]
        while self.page<page:
            self.apiurl='https://m.weibo.cn/api/container/getIndex?containerid=102803&page='+str(self.page)
            self.response_=requests.get(self.apiurl,timeout=3)
            if self.response_.status_code==200:
                self.res_=self.response_.json()
                if self.res_['ok']==1:
                    print("ok",self.page)
                    self.data_=self.res_['data']['cards']
                    for data in self.data_:
                        if data['card_type']==9:
                            self.data.append(data)
                            #print(data)
                else:
                    break
            time.sleep(2)
            self.page+=1




'''
db = pymysql.connect("localhost","root","nice.tv520","weibo")#打开数据库
cursor = db.cursor()
sql = "REPLACE INTO usr (id,screen_name,followers_count) VALUES "
data = ' '
cursor.execute(sql + data)
db.commit()
'''
#示例
if __name__ == "__main__":
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }

    # 类User_Weibo(userid=None,proxy=None,cookies=None,headers=None,**userdata)
    a = User_Weibo.getUserInfo(1911484643)
    # 静态方法：直接返回用户数据

    b = User_Weibo(1911484643)
    # 创建用户实例
    # >>>b.screen_name
    # >>>张三

    c = User_Weibo(userdata=b)
    # 无需访问服务器，使用已有用户数据创建用户实例

    # 类StatusesByUser_Weibo(1681029540)
    d = StatusesByUser_Weibo(1681029540)
    # 创建用户微博实例

    e = d.getStatuses(numberlimit=50,laststatusid=0,lasttime=0,proxy=None,cookies=None,headers=None)
    # 获取用户微博内容
    d.getStatuses()
    # >>>len(d.statusesDataAll)
    # >>>50
    # >>>len(d.statusesData)
    # >>>50
    d.getStatuses(numberlimit=20)
    # >>>len(d.statusesDataAll)
    # >>>70
    # >>>len(d.statusesData)
    # >>>20

    # 类Status_Weibo（statusid=None,proxy=None,cookies=None,headers=None,**statusdata)
    e = Status_Weibo(4314179525850390)
    # 创建微博实例
    # >>>e.text
    # >>>微博内容文本
    f = User_Weibo(userdata=e.user)
    # 使用微博中的用户信息创建用户实例
    # >>>f.screen_name
    # >>>张三
    g = Status_Weibo(statusdata=e.statusdata)
    # 无需访问服务器，使用已有微博数据创建微博实例

    '''
    hot=Hot_Weibo()
    #print(hot.data)
    data = ''
    for user in hot.data:
        userinfo=user['mblog']['user']
        if userinfo['followers_count']>100000:
            data_="('%s','%s','%s'),"%(str(userinfo['id']),userinfo['screen_name'],str(userinfo['followers_count']))
            #print(data_)
            data+=data_
            #print(userinfo['id'],userinfo['screen_name'],userinfo['followers_count'])
    '''


    '''


    db = pymysql.connect("localhost","root","nice.tv520","weibo")#打开数据库
    #db = pymysql.connect("120.27.151.217","root","nice.tv520","weibo")#打开数据库
    cursor = db.cursor()

    
    sql = "REPLACE INTO usr (id,screen_name,followers_count) VALUES "
    sql=sql+data[:-1]
    #print(sql)
    cursor.execute(sql)

    db.commit()
    
    x=0
    while x<4:

        cookies=RequestsTest().login_weibo('wangzheng@nicetv.com.cn','tcwz1234')
        userid=0
        while userid<9000000000:
            try:
                print('userid',userid)
                sql="SELECT id FROM usr WHERE id>%s and id<%s"%(userid,userid+1000000000)
                cursor.execute(sql)
                results=cursor.fetchall()
                print(results)
                for ids in results:
                    page=0
                    print(ids[0])
                    data=''
                    while True:
                        data_=[]
                        apiurl='https://m.weibo.cn/api/container/getIndex?containerid=231051_-_followers_-_'+str(ids[0])+'&page='+str(page)
                        response=requests.get(apiurl,cookies=cookies,timeout=3)
                        print(response.status_code)
                        if response.status_code==200:
                            res=response.json()
                            if res['ok']==1:
                                fans=res['data']['cards'][0]['card_group']
                                for fan in fans:
                                    if fan['card_type']==10:
                                        fandata=fan['user']
                                        if fandata['followers_count']>100000:
                                            print(fandata['screen_name'],fandata['followers_count'])
                                            data_="('%s','%s','%s'),"%(str(fandata['id']),fandata['screen_name'],str(fandata['followers_count']))
                                            data+=data_
                            else:
                                break
                        else:
                            break
                        time.sleep(0.3)
                        page+=1
                    sql = "REPLACE INTO usr (id,screen_name,followers_count) VALUES "
                    sql=sql+data[:-1]
                    print(sql)
                    try:
                        cursor.execute(sql)
                        db.commit()
                    except:
                        pass
            except:
                pass
            userid+=1000000000
        x+=1
        
    db.close()
    '''





    

