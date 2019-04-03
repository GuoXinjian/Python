#coding=utf-8

import urllib.request
import urllib.parse
import json
import re
import time
#import pymysql

def weiboStatusInfo(userId=[]):
    print('开始抓取微博内容数据：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('抓取每个博主前5页的微博内容')

    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }#模拟浏览器访问url
    
    resData = []
    
    i = 0
    while i < len(userId):
        #time.sleep(5)
        page=1
        while page<=5:#抓5页的数据-需要改进为抓上周的数据
            
            userUrl = 'https://m.weibo.cn/api/container/getIndex?containerid=107603'+str(userId[i])+'&page='+str(page) #访问博主状态信息
            userRequest = urllib.request.Request(userUrl,headers=header)
            userResponse = urllib.request.urlopen(userRequest).read()
            userData = json.loads(userResponse)#字符串转化为json对象
            n = 0
            while n<len(userData['data']['cards']):
                mblog = userData['data']['cards'][n]['mblog']
                resData_ = [0,0,0,0,0,0,0,0,0]
                if userData['data']['cards'][n]['card_type']==9:
                    resData_[0]=userId[i]
                    resData_[1]=mblog['user']['screen_name']
                    resData_[2]=mblog['id']
                    resData_[3]=mblog['created_at']
                    resData_[4]=re.sub("<[^>]+>","",mblog['text']) #使用正则表达式去掉标签和链接
                    resData_[5]=mblog['reposts_count']
                    resData_[6]=mblog['comments_count']
                    resData_[7]=mblog['attitudes_count']
                    try:
                        resData_[8]=mblog['obj_ext']
                    except:
                        resData_[8]=None
                    n+=1
                    resData.append(resData_)
                else:
                    n+=1
            page+=1
        i+=1
    return resData

#res=weiboUserInfo()
#print(res)

