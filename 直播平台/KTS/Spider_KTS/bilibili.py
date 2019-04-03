#coding=utf-8

import urllib.request
import urllib.parse
import json
#import re
import time
#import pymysql

def bilibili(userId=[]):
    print('开始抓取bilibili内容数据：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('抓取前25个视频')

    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }#模拟浏览器访问url
    
    resData = []
    i = 0
    while i < len(userId):

        urlHead = 'https://space.bilibili.com/ajax/member/getSubmitVideos?pagesize=50&mid=' 
        page = 1
        while page<=1:
            header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
            }#模拟浏览器访问url
            videoRequest = urllib.request.Request(urlHead+str(userId[i])+'&page='+str(page),headers=header)
            vidoeResponse = urllib.request.urlopen(videoRequest).read()
            #print(vidoeResponse)
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
            page+=1
        i+=1
    #print(resData)
    return resData

#res=weiboUserInfo()
#print(res)

#bilibili(['32754699'])