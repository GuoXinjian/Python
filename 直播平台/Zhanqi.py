#coding=utf-8

import urllib.request
import urllib.parse
import json
import time



def zhanqi(page):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
    url_zhanqiapi = 'https://www.zhanqi.tv/api/static/v2.1/live/list/120/'
    current_page = 1 
    urlend_zhanqiapi = '.json'
    roomid = []
    userid = []
    username = []
    title = []
    hot_index = []
    game = []
    

    while current_page <= page:#抓取'page'页数据 每页120个主播
        zhanqiRequest = urllib.request.Request(url_zhanqiapi+'%s'%current_page+urlend_zhanqiapi,headers=header)
        zhanqiReponse = urllib.request.urlopen(zhanqiRequest).read()
        zhanqiData = json.loads(zhanqiReponse)#字符串转化为json对象
        numsOfRoom = len(zhanqiData['data']['rooms'])
        #print(numsOfRoom)
        i = 0
        time.sleep(5)
        while i < numsOfRoom:
            #print(zhanqiData['data']['rl'][i]['rid'] ,zhanqiData['data']['rl'][i]['rn'],zhanqiData['data']['rl'][i]['nn'])
            roomid.append(zhanqiData['data']['rooms'][i]['code'])
            userid.append(zhanqiData['data']['rooms'][i]['uid'])
            username.append(zhanqiData['data']['rooms'][i]['nickname'])
            title.append(zhanqiData['data']['rooms'][i]['title'])
            hot_index.append(zhanqiData['data']['rooms'][i]['online'])
            game.append(zhanqiData['data']['rooms'][i]['newGameName'])
            i += 1
        current_page += 1
    #print([roomid,userid,username,title,hot_index,game])
    #print(len(userid))
    return [roomid,userid,username,title,hot_index,game]

#zhanqi(3)