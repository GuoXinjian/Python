#coding=utf-8

import urllib.request
import urllib.parse
import json
import time



def panda(page):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
    url_pandaapi = 'https://www.panda.tv/live_lists?status=2&token=&pagenum=120&order=top&pageno='
    current_page = 1 
    roomid = []
    userid = []
    username = []
    title = []
    hot_index = []
    game = []
    

    while current_page <= page:#抓取'page'页数据 每页120个主播
        pandaRequest = urllib.request.Request(url_pandaapi+'%s'%current_page,headers=header)
        pandaReponse = urllib.request.urlopen(pandaRequest).read()
        pandaData = json.loads(pandaReponse)#字符串转化为json对象
        numsOfRoom = len(pandaData['data']['items'])
        #print(numsOfRoom)
        i = 0
        
        while i < numsOfRoom:
            #print(pandaData['data']['rl'][i]['rid'] ,pandaData['data']['rl'][i]['rn'],pandaData['data']['rl'][i]['nn'])
            roomid.append(pandaData['data']['items'][i]['id'])
            userid.append(pandaData['data']['items'][i]['userinfo']['rid'])
            username.append(pandaData['data']['items'][i]['userinfo']['nickName'])
            title.append(pandaData['data']['items'][i]['name'])
            hot_index.append(pandaData['data']['items'][i]['person_num'])
            game.append(pandaData['data']['items'][i]['classification']['cname'])
            i += 1
        current_page += 1
    #print([roomid,userid,username,title,hot_index,game])
    #print(len(userid))
    return [roomid,userid,username,title,hot_index,game]

#panda(3)