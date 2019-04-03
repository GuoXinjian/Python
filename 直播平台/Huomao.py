#coding=utf-8

import urllib.request
import urllib.parse
import json
import time



def huomao(page):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
    url_huomaoapi = 'https://www.huomao.com/channels/channelnew.json?game_url_rule=all&page='
    current_page = 1 
    roomid = []
    userid = []
    username = []
    title = []
    hot_index = []
    game = []
    

    while current_page <= page:#抓取'page'页数据 每页120个主播
        huomaoRequest = urllib.request.Request(url_huomaoapi+'%s'%current_page,headers=header)
        huomaoReponse = urllib.request.urlopen(huomaoRequest).read()
        huomaoData = json.loads(huomaoReponse)#字符串转化为json对象
        numsOfRoom = len(huomaoData['data']['channelList'])
        #print(numsOfRoom)
        i = 0
        time.sleep(5)
        while i < numsOfRoom:
            #print(huomaoData['data']['rl'][i]['rid'] ,huomaoData['data']['rl'][i]['rn'],huomaoData['data']['rl'][i]['nn'])
            roomid.append(huomaoData['data']['channelList'][i]['room_number'])
            userid.append(huomaoData['data']['channelList'][i]['uid'])
            username.append(huomaoData['data']['channelList'][i]['nickname'])
            title.append(huomaoData['data']['channelList'][i]['channel'])
            hot_index.append(huomaoData['data']['channelList'][i]['originviews'])
            game.append(huomaoData['data']['channelList'][i]['gameCname'])
            i += 1
        current_page += 1
    #print([roomid,userid,username,title,hot_index,game])
    return [roomid,userid,username,title,hot_index,game]

