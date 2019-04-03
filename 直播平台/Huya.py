#coding=utf-8

import urllib.request
import urllib.parse
import json
import time



def huya(page):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
    url_huyaapi = 'https://www.huya.com/cache.php?m=LiveList&page='
    current_page = 1 
    roomid = []
    userid = []
    username = []
    title = []
    hot_index = []
    game = []
    time.sleep(5)

    while current_page <= page:#抓取'page'页数据 每页120个主播
        huyaRequest = urllib.request.Request(url_huyaapi+'%s'%current_page,headers=header)
        huyaReponse = urllib.request.urlopen(huyaRequest).read()
        huyaData = json.loads(huyaReponse)#字符串转化为json对象
        numsOfRoom = len(huyaData['data']['datas'])
        #print(numsOfRoom)
        i = 0
        
        while i < numsOfRoom:
            #print(huyaData['data']['rl'][i]['rid'] ,huyaData['data']['rl'][i]['rn'],huyaData['data']['rl'][i]['nn'])
            roomid.append(huyaData['data']['datas'][i]['profileRoom'])
            userid.append(huyaData['data']['datas'][i]['uid'])
            username.append(huyaData['data']['datas'][i]['nick'])
            title.append(huyaData['data']['datas'][i]['introduction'])
            hot_index.append(huyaData['data']['datas'][i]['totalCount'])
            game.append(huyaData['data']['datas'][i]['gameFullName'])
            i += 1
        current_page += 1
    #print([roomid,userid,username,title,hot_index,game])
    return [roomid,userid,username,title,hot_index,game]
#huya(3)
