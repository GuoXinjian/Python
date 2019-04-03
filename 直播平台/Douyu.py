#coding=utf-8

import urllib.request
import urllib.parse
import json
import time



def douyu(page):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
    url_douyuapi = 'https://www.douyu.com/gapi/rkc/directory/0_0/'
    current_page = 1 
    roomid = []
    userid = []
    username = []
    title = []
    hot_index = []
    game = []
    

    while current_page <= page:#抓取'page'页数据 每页120个主播
        douyuRequest = urllib.request.Request(url_douyuapi+'%s'%current_page,headers=header)
        douyuReponse = urllib.request.urlopen(douyuRequest).read()
        douyuData = json.loads(douyuReponse)#字符串转化为json对象
        numsOfRoom = len(douyuData['data']['rl'])
        #print(numsOfRoom)
        i = 0
        time.sleep(5)
        while i < numsOfRoom:
            #print(douyuData['data']['rl'][i]['rid'] ,douyuData['data']['rl'][i]['rn'],douyuData['data']['rl'][i]['nn'])
            roomid.append(douyuData['data']['rl'][i]['rid'])
            userid.append(douyuData['data']['rl'][i]['uid'])
            username.append(douyuData['data']['rl'][i]['nn'])
            title.append(douyuData['data']['rl'][i]['rn'])
            hot_index.append(douyuData['data']['rl'][i]['ol'])
            game.append(douyuData['data']['rl'][i]['c2name'])
            i += 1
        current_page += 1
    #print([roomid,userid,username,title,hot_index,game])
    return [roomid,userid,username,title,hot_index,game]

#douyu(3)