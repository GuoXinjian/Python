#coding=utf-8

import urllib.request
import urllib.parse
import json
import re
import time
#import pymysql

def weiboUserInfo(userId=[]):
    
    print('开始抓取微博个人信息：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }#模拟浏览器访问url
    '''
    userId = [
        '5165342772',#@陈正CAT
        '2202350975',#微雅
        '6074356560',#KPL官博
        '6627980190',
        '6062063357',
        '2703348994',
        '2609737945',
        '6134425922',
        '6383293935',
        '6606870891',
        '6528198786',
        '5953944527',
        '6451712914',
        '6134307924',
        '6628651635',
        '6329212263',
        '6180100850',
        '6025941641',
        '6320517591',
        '6004095423',
        '6001960114',
        '1811893237',
        '5698023579',
        '6058108621',
        '1965586127',
        '5508734253',
        '2566133010',
        '5816037017',
        '3160116133',
        '1531609254',
        '5687445105',
        '5072496178',
        '2219238114',
        '2662750333',
        '2950251663'

    ]#需要查询的微博博主的id
    '''
    resData = [[0 for col in range(7)] for row in range(len(userId))]
    
    i = 0
    while i < len(userId):
        #time.sleep(5)
        userUrl = 'https://m.weibo.cn/api/container/getIndex?containerid=100505'+str(userId[i]) #访问博主个人信息
        userRequest = urllib.request.Request(userUrl,headers=header)
        userResponse = urllib.request.urlopen(userRequest).read()
        userData = json.loads(userResponse)#字符串转化为json对象
        userName = userData['data']['userInfo']['screen_name']
        #print(userId)
        statusCount = userData['data']['userInfo']['statuses_count']           
        description = userData['data']['userInfo']['description']
        followersCount = userData['data']['userInfo']['followers_count']
        followCount = userData['data']['userInfo']['follow_count']
        
        try:
            userUrl = 'https://m.weibo.cn/api/container/getIndex?containerid=231567'+userId[i]#访问博主视频信息
            userRequest = urllib.request.Request(userUrl,headers=header)
            userResponse = urllib.request.urlopen(userRequest).read()
            userData = json.loads(userResponse)#字符串转化为json对象
            videoCount = userData['data']['cardlistInfo']['total']
        except:
            videoCount = 0
        
        resData[i][0]=userId[i]
        resData[i][1]=userName
        resData[i][2]=description
        resData[i][3]=statusCount
        resData[i][4]=videoCount
        resData[i][5]=followersCount
        resData[i][6]=followCount
        #print(resData[i])
        i+=1
    return resData

#res=weiboUserInfo()
#print(res)

