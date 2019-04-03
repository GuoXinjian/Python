import urllib.request #url请求
import urllib.parse #url解析
from bs4 import BeautifulSoup #以正则匹配html
import datetime
import logging
import re

# 数值处理
def toInt(str):
    if 'w' in str or '万' in str:
        num = float(re.findall(r"\d+\.?\d*", str)[0])
        num = int(num * 10000)
    else:
        num = int(re.findall(r"\d+\.?\d*", str)[0])
    return num

# 快手用户实体类
class user():
    # 构造函数
    def __init__(self, id):
        # 拼接url
        self.url = 'http://i.youku.com/i/' + id + '/videos'
        self.name = ''
        self.description = ''
        self.fanNum = 0
        self.videoPlayNumAll = 0
        self.videoNum = 0
        # [标题，发布时间，播放，点赞，评论]
        self.videoList = []
        self.spider()
        # self.date = datetime.datetime.now().strftime('%Y-%m-%d')
        # self.time = datetime.datetime.now().strftime('%H:%M:%S')
        # self.week = datetime.datetime.now().isocalendar()
    # 爬虫主函数
    def spider(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded;charset = UTF - 8',
            'Origin': 'https://www.youku.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
        }  # 模拟浏览器访问url

        request = urllib.request.Request(self.url, headers=header)

        response = urllib.request.urlopen(request).read()
        html =str(response,'utf-8')
        soup = BeautifulSoup(html, "lxml")
        # print(soup)
        # 用户基本信息
        # self.name = soup.find('div',attrs={'class':'user-name'}).contents[0].string.strip()
        self.name = soup.find('a', attrs={'class': 'username'}).string
        self.fanNum = int(soup.find('li', attrs={'class': 'snum'}).get('title').replace(',', ''))
        self.videoPlayNumAll = int(soup.find('li', attrs={'class': 'vnum'}).get('title').replace(',',''))
        self.videoNum = toInt(soup.find('div', attrs={'class': 'title'}).find('span').string.strip())
        # print(soup.find('div', attrs={'class': 'title'}).find('span'))

        # 处理视频信息
        # 视频标题、发布时间、播放量
        videoCode= soup.find_all('div', attrs={'class': 'v-meta'})
        # print(toInt(videoCode[0].find('span', attrs={'class': 'v-num'}).string))
        for i in range(len(videoCode)):
            try:
                title =videoCode[i].find('div', attrs={'class': 'v-meta-title'}).contents[0].get('title')
                publishTime = videoCode[i].find('span', attrs={'class': 'v-publishtime'}).string
                playNum = toInt(videoCode[i].find('span', attrs={'class': 'v-num'}).string)
                self.videoList.append([title,publishTime,playNum])
            except Exception as e:
                title = videoCode[i].find('div', attrs={'class': 'v-meta-title'}).string
                self.videoList.append([title, '',0 ])
                logging.exception(e)


# 列表类
class youKuList():
    def __init__(self, idPool):
        self.idPool = []
        for i in range(len(idPool)):
            self.idPool.append(idPool[i])
        self.user = []
        for i in range(len(self.idPool)):
            self.user.append(user(self.idPool[i]))

    # 外部用户信息接口
    def getUserInfo(self):
        userInfo = []
        for i in range(len(self.user)):
            # 用户ID、粉丝数、视频播放总量、视频数
            userInfo.append(
                [self.user[i].name, self.user[i].fanNum, self.user[i].videoPlayNumAll, self.user[i].videoNum]
            )
        # for i in range(len(userInfo)):
        #     print(userInfo[i])
        return userInfo

    # 外部视频信息接口
    def getVideoInfo(self):
        videoInfo = []
        for i in range(len(self.user)):
            for j in range(len(self.user[i].videoList)):
                # 用户ID、标题、发布时间、 播放
                videoInfo.append(
                    [self.user[i].name, self.user[i].videoList[j][0], self.user[i].videoList[j][1],
                     self.user[i].videoList[j][2]]
                )
        # for i in range(len(videoInfo)):
        #     print(videoInfo[i])
        return videoInfo
#
# idPool = ['UMTcyNDA0MDE1Ng==']
# youKuList = youKuList(idPool)
# youKuList.getUserInfo()
# youKuList.getVideoInfo()

