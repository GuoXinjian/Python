import requests
import time,datetime

class DouyuByHot():
    
    @staticmethod
    def getInfo(roomNum = 240):
        i = 1
        page = roomNum // 120 + (1 if roomNum % 120 else 0)
        url = 'https://www.douyu.com/gapi/rkc/directory/0_0/'
        data=[]
        while i<=page:
            roomList = requests.get(url+str(i)).json()
            roomList = roomList['data']['rl']
            for r in roomList:
                #print(r)
                if len(data)<roomNum:
                    data.append(r)
                else:
                    break
            i += 1
        print('douyu',len(data))
        return data

class EgameByHot():
    
    @staticmethod
    def getInfo(roomNum = 240):
        i = 1
        page = roomNum // 120 + (1 if roomNum % 120 else 0)
        url = 'https://share.egame.qq.com/cgi-bin/pgg_live_async_fcgi?param={"key":{"module":"pgg_live_read_ifc_mt_svr","method":"get_pc_live_list","param":{"appid":"hot","page_num":'
        urlend = ',"page_size":120}}}'
        # url = 'https://share.egame.qq.com/cgi-bin/pgg_live_async_fcgi?param=%7B%22key%22:%7B%22module%22:%22pgg_live_read_ifc_mt_svr%22,%22method%22:%22get_pc_live_list%22,%22param%22:%7B%22appid%22:%22hot%22,%22page_num%22:8,%22page_size%22:40,%22tag_id%22:0,%22tag_id_str%22:%22%22%7D%7D%7D'
        data=[]
        while i<=page:
            roomList = requests.get(url+str(i)+urlend).json()
            roomList = roomList['data']['key']['retBody']['data']['live_data']['live_list']
            for r in roomList:
                #print(r)
                if len(data)<roomNum:
                    data.append(r)
                else:
                    break
            i += 1
        print('egame',len(data))
        return data

class HuomaoByHot():
    
    @staticmethod
    def getInfo(roomNum = 120):
        i = 1
        page = roomNum // 60 + (1 if roomNum % 120 else 0)
        url = 'https://www.huomao.com/channels/channelnew.json?game_url_rule=all&page='
        data=[]
        while i<=page:
            roomList = requests.get(url+str(i)).json()
            roomList = roomList['data']['channelList']
            for r in roomList:
                #print(r)
                if len(data)<roomNum:
                    data.append(r)
                else:
                    break
            i += 1
        print('huomao',len(data))
        return data

class HuyaByHot():

    @staticmethod
    def getInfo(roomNum = 120):
        i = 1
        page = roomNum // 120 + (1 if roomNum % 120 else 0)
        url = 'https://www.huya.com/cache.php?m=LiveList&page='
        data=[]
        while i<=page:
            roomList = requests.get(url+str(i)).json()
            roomList = roomList['data']['datas']
            for r in roomList:
                #print(r)
                if len(data)<roomNum:
                    data.append(r)
                else:
                    break
            i += 1
        print('huya',len(data))
        return data

class PandaByHot():

    @staticmethod
    def getInfo(roomNum = 120):
        i = 1
        page = roomNum // 120 + (1 if roomNum % 120 else 0)
        url = 'https://www.panda.tv/live_lists?status=2&token=&pagenum=120&order=top&pageno='
        data=[]
        while i<=page:
            roomList = requests.get(url+str(i)).json()
            roomList = roomList['data']['items']
            for r in roomList:
                #print(r)
                if len(data)<roomNum:
                    data.append(r)
                else:
                    break
            i += 1
        print('panda',len(data))
        return data

class ZhanqiByHot():

    @staticmethod
    def getInfo(roomNum = 120):
        i = 1
        page = roomNum // 120 + (1 if roomNum % 120 else 0)
        url = 'https://www.zhanqi.tv/api/static/v2.1/live/list/120/'
        urlend = '.json'
        data=[]
        #count=0
        while i<=page:
            roomList = requests.get(url+str(i)+urlend).json()
            roomList = roomList['data']['rooms']
            for r in roomList:
                #print(r)
                #count+=1
                if len(data)<roomNum:
                    data.append(r)
                else:
                    break
            i += 1
        print('zhanqi',len(data))
        return data




if __name__ == '__main__':
    print(time.time())
    data = DouyuByHot.getInfo()
    print(time.time())