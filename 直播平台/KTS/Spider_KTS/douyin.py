#coding=utf-8

import urllib.request
import urllib.parse
import json
#import re
import time
#import pymysql

def bilibili(userId=[]):
    print('开始抓取bilibili内容数据：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    #print('抓取前25个视频')

    header = {
    'User-Agent': 'okhttp/3.10.0.1'
    }#模拟浏览器访问url
    
    resData = []
    i = 0
    while i < len(userId):

        urlHead = 'http://aweme.snssdk.com/aweme/v1/aweme/post/?user_id=104205087905&count=20&aid=1128&language=zh&os_api=22&os_version=5.1.1&uuid=867757555422788&openudid=5091046277557885&manifest_version_code=270&resolution=1280*720&dpi=192&update_version_code=2702&_rticket=1538211624985&ts=1538211624&as=a125239a6812dbbfdf4355&cp=3c27b15d8bf2a4f5e1%5BcIg&mas=011893d3bc6602bffe0ffa51db7147467facaccc2c662666464626' 
        #urlHead = 'http://aweme.snssdk.com/aweme/v1/aweme/post/?max_cursor=0&user_id=104205087905&count=20&retry_type=no_retry&iid=44448106687&device_id=57588300691&ac=wifi&channel=wandoujia&aid=1128&app_name=aweme&version_code=270&version_name=2.7.0&device_platform=android&ssmix=a&device_type=SM-G925F&device_brand=samsung&language=zh&os_api=22&os_version=5.1.1&uuid=867757555422788&openudid=5091046277557885&manifest_version_code=270&resolution=1280*720&dpi=192&update_version_code=2702&_rticket=1538211624985&ts=1538211624&as=a125239a6812dbbfdf4355&cp=3c27b15d8bf2a4f5e1%5BcIg&mas=011893d3bc6602bffe0ffa51db7147467facaccc2c662666464626' 
        
        urlHead = 'http://aweme.snssdk.com/aweme/v1/aweme/post/?max_cursor=0&user_id=104205087905&count=20&retry_type=no_retry&iid=44448106687&device_id=57588300691&ac=wifi&channel=wandoujia&aid=1128&app_name=aweme&version_code=270&version_name=2.7.0&device_platform=android&ssmix=a&device_type=SM-G925F&device_brand=samsung&language=zh&os_api=22&os_version=5.1.1&uuid=867757555422788&openudid=5091046277557885&manifest_version_code=270&resolution=1280*720&dpi=192&update_version_code=2702&_rticket=1538213093487&ts=1538213093&as=a1f5d4da85ee6b54cf4355&cp=43ebb85457fda844e1acOg&mas=01ff67a7571deb5c345bd93b267d728f03acaccc2c66c62cac466c'
        page = 1
        while page<=1:
            header = {
            'User-Agent': 'okhttp/3.10.0.1'
            }#模拟浏览器访问url
            videoRequest = urllib.request.Request(urlHead,headers=header)
            vidoeResponse = urllib.request.urlopen(videoRequest).read()
            print(vidoeResponse)
            Data = json.loads(vidoeResponse)
            print(Data)
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

bilibili(['131247100'])