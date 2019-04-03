#coding=utf-8

import urllib.request
import urllib.parse
import json
import time

#企鹅直播可以直接读粉丝数和主播所在地

def egame(page):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'}
    url_egameapi = 'https://share.egame.qq.com/cgi-bin/pgg_live_async_fcgi?param=%7B"key":%7B"module":"pgg_live_read_ifc_mt_svr","method":"get_pc_live_list","param":%7B"appid":"hot","page_num":'
    current_page = 1 
    urlend_egameapi = ',"page_size":40,"tag_id":0,"tag_id_str":""%7D%7D%7D'
    roomid = []
    userid = []
    username = []
    title = []
    hot_index = []
    game = []
    

    while current_page <= page:#抓取'page'页数据 每页120个主播
        egameRequest = urllib.request.Request(url_egameapi+'%s'%current_page+urlend_egameapi,headers=header)
        egameReponse = urllib.request.urlopen(egameRequest).read()
        egameData_pre = json.loads(egameReponse)#字符串转化为json对象
        egameData = egameData_pre['data']['key']['retBody']
        numsOfRoom = len(egameData['data']['live_data']['live_list'])
        #print(numsOfRoom)
        i = 0
        time.sleep(5)
        while i < numsOfRoom:
            #print(egameData['data']['rl'][i]['rid'] ,egameData['data']['rl'][i]['rn'],egameData['data']['rl'][i]['nn'])
            roomid.append(egameData['data']['live_data']['live_list'][i]['anchor_id'])
            userid.append(egameData['data']['live_data']['live_list'][i]['appid'])
            username.append(egameData['data']['live_data']['live_list'][i]['anchor_name'])
            title.append(egameData['data']['live_data']['live_list'][i]['title'])
            hot_index.append(egameData['data']['live_data']['live_list'][i]['online'])
            game.append(egameData['data']['live_data']['live_list'][i]['appname'])
            i += 1
        current_page += 1
    #print([roomid,userid,username,title,hot_index,game])
    print(len(userid))
    return [roomid,userid,username,title,hot_index,game]

egame(3)