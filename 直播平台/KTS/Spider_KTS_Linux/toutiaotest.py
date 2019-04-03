#coding=utf-8

import urllib.request
import urllib.parse
import json
#import re
import time
#import pymysql

def bilibili(userId=[]):
    print('开始抓取toutiao内容数据：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('抓取前25个视频')

    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }#模拟浏览器访问url
    
    resData = []
    i = 0
    while i < len(userId):

        urlHead = 'http://i.snssdk.com/dongtai/list/v9/?user_id=104204887690&callback=jsonp1' 
        page = 1
        while page<=1:
            header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
            'cookie': 'csrftoken=a04a0fe56fb7d9c2815374c6d6b39f5a; tt_webid=6606540219507033604; __tasessionId=lk562alrk1538205013983; uuid="w:bef906c2f5484362931eb842d78f39f1"; UM_distinctid=1662429d83944a-02d5abf4d554db-8383268-1fa400-1662429d83a62a; CNZZDATA1259612802=727726284-1538201542-https%253A%252F%252Fask.csdn.net%252F%7C1538201542',
            'upgrade-insecure-requests': '1',
            'authority': 'www.toutiao.com',
            'method': 'GET',
            'path': '/c/user/article/?page_type=1&user_id=104204887690&max_behot_time=0&count=20&as=A1557B4AEF22963&cp=5BAFE229A6B31E1&_signature=B12kGRAbXPitcuSZxGWItwddpA',

            }#模拟浏览器访问url
            videoRequest = urllib.request.Request(urlHead,headers=header)
            vidoeResponse = urllib.request.urlopen(videoRequest).read()
            print(vidoeResponse.decode())
            '''
            Data = json.loads(vidoeResponse)
            #print(Data)
            j = 0
            while j < len(Data['data']['vlist']):
                vid = Data['data']['vlist'][j]['aid']
                title = Data['data']['vlist'][j]['title']
                created = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(Data['data']['vlist'][j]['created']))
                desc = Data['data']['vlist'][j]['description']
                play = Data['data']['vlist'][j]['play']
                comment = Data['data']['vlist'][j]['comment']
                favorites = Data['data']['vlist'][j]['favorites']
                resData.append([userId[i],vid,title,created,desc,play,comment,favorites])
                j+=1
                '''
            page+=1
        i+=1
    #print(resData)
    return resData

#res=weiboUserInfo()
#print(res)

bilibili(['131247100'])