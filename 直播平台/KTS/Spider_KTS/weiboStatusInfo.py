#coding=utf-8

import urllib.request
import urllib.parse
import json
import re
import time
#import pymysql

def toInt(str):
    if str == 'None':
        return 0
    if 'w' in str or '万' in str:
        num = float(re.findall(r"\d+\.?\d*", str)[0])
        num = int(num * 10000)
    else:
        num = int(re.findall(r"\d+\.?\d*", str)[0])
    return num

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
            try:
                userUrl = 'https://m.weibo.cn/api/container/getIndex?containerid=107603'+str(userId[i])+'&page='+str(page) #访问博主状态信息
                userRequest = urllib.request.Request(userUrl,headers=header)
                userResponse = urllib.request.urlopen(userRequest).read()
                userData = json.loads(userResponse)#字符串转化为json对象
                n = 0
                while n<len(userData['data']['cards']):
                    
                    resData_ = [0,0,0,0,0,0,0,0,0]
                    if userData['data']['cards'][n]['card_type']==9:
                        mblog = userData['data']['cards'][n]['mblog']
                        resData_[0]=userId[i]
                        resData_[1]=mblog['user']['screen_name']
                        resData_[2]=mblog['id']
                        resData_[3]=mblog['created_at']
                        resData_[4]=re.sub("<[^>]+>","",mblog['text']) #使用正则表达式去掉标签和链接
                        resData_[5] = toInt(str(mblog['reposts_count']))
                        resData_[6] = toInt(str(mblog['comments_count']))
                        resData_[7] = toInt(str(mblog['attitudes_count']))
                        try:
                            if mblog['retweeted_status']!='':
                                resData_[8]=None
                        except:
                            try:
                                resData_[8] = toInt(mblog['obj_ext'])
                            except:
                                resData_[8]=None
                        n+=1
                        resData.append(resData_)
                    else:
                        n+=1
            except:
                pass
            page+=1
        i+=1
    return resData


'''
res=weiboStatusInfo(['3158585791'])
for i in range(len(res)):
     print(res[i])
'''
