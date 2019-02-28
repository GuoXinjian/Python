import requests
import time,re,json
from bs4 import BeautifulSoup,SoupStrainer

def toInt(string):
    string = re.sub(',','',string)
    if 'w' in string or '万' in string:
        num = float(re.findall(r"\d+\.?\d*", string)[0])
        num = int(num * 10000)
    else:
        num = int(re.findall(r"\d+\.?\d*", string)[0])
    return num
class YoukuByUser():

    @staticmethod
    def getVideoInfo(userid,roomNum = 100,proxy=None):
        i = 1
        page = roomNum // 50 + (1 if roomNum % 50 else 0)
        url = 'http://i.youku.com/i/' + str(userid) + '/videos?page='+str(page)
        data = []
        while i<=page:
            response = requests.get(url,timeout=3,proxies=proxy).content
            tag = SoupStrainer('div',{'class':'v va'})
            username = BeautifulSoup(response,'lxml',parse_only=SoupStrainer('a',{'class':'username'})).find('a',{'class':'username'}).get('title')
            soup = BeautifulSoup(response,'lxml',parse_only=tag)
            videoList = soup.find_all('div',{'class':'v va'})
            for video in videoList:
                videoinfo = video.find('div',{'class':'v-link'}).contents[0]
                title = videoinfo.get('title')
                vid = videoinfo.get('href')[24:-5]
                try:
                    publishtime = video.find('span',{'class':'v-publishtime'}).string
                    count = toInt(video.find('span',{'class':'v-num'}).string)
                except:
                    count = 0
                    publishtime = '私密文件不公开显示'
                #print(title,vid,count,publishtime)
                data.append({'username':username,'userid':userid,'vid':vid,'title':title,'count':count,'publishtime':publishtime})
            i+=1
        return data
    
    @staticmethod
    def getUserInfo(userid,proxy=None):
        url = 'http://i.youku.com/i/' + str(userid)
        data =[]
        response = requests.get(url,timeout=3,proxies=proxy).content
        tag = SoupStrainer('div',{'class':'head-info'})
        soup = BeautifulSoup(response,'lxml',parse_only=tag)
        username = soup.find('a',{'class':'username'}).get('title')
        count = toInt(soup.find('li',{'class':'vnum'}).get('title'))
        fans = toInt(soup.find('li',{'class':'snum'}).get('title'))
        data.append({'username':username,'userid':userid,'count':count,'fans':fans})
        #print(data)
        return data

class VQQByUser():
    @staticmethod
    def getVideoInfo(userid,roomNum = 120,proxy=None):
        username = BeautifulSoup(requests.get('http://v.qq.com/vplus/' + str(userid),proxies=proxy).content,'lxml',parse_only=SoupStrainer(id='userInfoNick')).find('span').string
        #print(username)
        i = 1
        page = roomNum // 30 + (1 if roomNum % 30 else 0)
        url = 'http://c.v.qq.com/vchannelinfo?otype=json&qm=1&num=30&uin=' + str(userid)+'&pagenum='+str(page)
        data = []
        while i<=page:
            response = requests.get(url,timeout=3,proxies=proxy).text
            response = json.loads(re.findall(r'({.*})',response)[0])
            #print(response)
            videoList = response['videolst']
            for v in videoList:
                v['userid']=userid
                v['username']=username
                v['play_count']=str(toInt(v['play_count']))
                #print(v)
                data.append(v)
            i+=1
        return data
    
    @staticmethod
    def getUserInfo(userid,proxy=None):
        url = 'http://v.qq.com/vplus/' + str(userid)
        data =[]
        response = requests.get(url,timeout=3,proxies=proxy).content
        tag = SoupStrainer('div',{'class':'mod_user_info'})
        soup = BeautifulSoup(response,'lxml',parse_only=tag)
        username = soup.find('span',id='userInfoNick').string
        #print(username)
        desc = soup.find('div',{'class':'user_intro'}).find('span',{'class':'txt'}).string
        usercount = soup.find('ul',{'class':'user_count'}).find_all('span',{'class':'num'})
        bookcount = toInt(usercount[0].string)
        videocount = usercount[1].string
        playcount = toInt(usercount[3].string)
        data.append({'username':username,'userid':userid,'playcount':playcount,'bookcount':bookcount,'videocount':videocount})
        #print(data)
        return data

class BilibiliByUser():

    @staticmethod
    def getUserInfo(userid,proxy=None):
        url = 'https://api.bilibili.com/x/space/acc/info?jsonp=jsonp&mid='+str(userid)
        response = requests.get(url,proxies=proxy).json()
        data = response['data']
        print(data)
        return data

    @staticmethod
    def getVideoInfo(userid,roomNum = 100,proxy=None):
        i = 1
        page = roomNum // 50 + (1 if roomNum % 50 else 0)
        url = 'https://space.bilibili.com/ajax/member/getSubmitVideos?pagesize=50&mid=' + str(userid) + '&page=' + str(page)
        data=[]
        while i<=page:
            roomList = requests.get(url,proxies=proxy).json()
            roomList = roomList['data']['vlist']
            for r in roomList:
                print(r)
                data.append(r)
            i += 1
        print('bilibiliVideo',len(data))
        return data

class WeishiByUser():

    @staticmethod
    def getUserInfo(userid,proxy=None):
        header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',}
        url = 'https://h5.weishi.qq.com/weishi/personal/'+str(userid) #访问博主信息
        response = requests.get(url,headers=header,proxies=proxy).content
        tag = SoupStrainer('div',{'class':'infor'})
        soup = BeautifulSoup(response,'lxml',parse_only=tag)
        name = soup.find_all('span',attrs={'class':'name'})[0].string
        desc = soup.find_all('p',attrs={'class':'description'})[0].string
        fans = toInt(soup.find_all('span',attrs={'class':'num j-numeric-fans'})[0].string)
        follow = toInt(soup.find_all('span',attrs={'class':'num j-numeric-interest'})[0].string)
        praise = toInt(soup.find_all('span',attrs={'class':'num j-numeric-receivepraise'})[0].string)
        data={'userid':userid,'name':name,'desc':desc,'fans':fans,'follow':follow,'praise':praise}
        print(data)
        return data

    @staticmethod
    def getVideoInfo(userid,proxy=None):
        header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',}
        url = 'https://h5.weishi.qq.com/weishi/personal/'+str(userid) #访问博主信息
        data=[]
        response = requests.get(url,headers=header,proxies=proxy).content
        tag = SoupStrainer('li')
        soup = BeautifulSoup(response,'lxml',parse_only=tag)

        videoid = soup.find_all('li',{'class':'figure-item j-figure-item'})
        play = soup.find_all('b')
        j = 0
        while j<len(videoid):
            data.append({'userid':userid,'videoid':videoid[j].attrs['data-id'],'play':toInt(play[j].string)})
            j+=1
        print(data)
        return data


class XiguaByUser():

    @staticmethod
    def getUserInfo(userid,proxy=None):
        header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',}
        url = 'https://www.ixigua.com/c/user/'+ str(userid)
        response = requests.get(url,headers=header,proxies=proxy).content
        soup = BeautifulSoup(response,'lxml')
        #print(soup)
        name = soup.find_all('h1',{'class':'tt-font-7'})[0].string
        desc = soup.find_all('p',{'class':'desc'})[0].string
        fans = soup.find_all('p',{'class':'num tt-font-7'})[0].string[:-3]
        data = {'userid':userid,'name':name,'desc':desc,'fans':fans}
        #print(data)
        return data
    
    @staticmethod
    def getVideoInfo(userid,roomNum = 30,proxy=None):
        header = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',}
        url='https://www.ixigua.com/c/user/article/?user_id=' + str(userid) + '&count='+str(roomNum)
        response = requests.get(url,headers=header,proxies=proxy).json()
        data=[]
        videoList=response['data']
        #print(videoList)
        for v in videoList:
            data.append(v)
            print(v)
        return data
    
class Chushou():
    @staticmethod
    def getUserInfo(userid,proxy=None):
        pass


if __name__ == "__main__":
    # YoukuByUser.getUserInfo('UNDk3MDA3NTYyMA==')
    # YoukuByUser.getVideoInfo('UNDk3MDA3NTYyMA==')
    # VQQByUser.getVideoInfo('bd91e789be690a85a6cc1771221b2ef5')
    # VQQByUser.getUserInfo('bd91e789be690a85a6cc1771221b2ef5')
    # BilibiliByUser.getUserInfo(32754699)
    # BilibiliByUser.getVideoInfo(32754699)
    # WeishiByUser.getVideoInfo(1526460070936802)
    # XiguaByUser.getUserInfo(67870829304)
    XiguaByUser.getVideoInfo(67870829304)