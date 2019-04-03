import urllib.request #url请求
import urllib.parse #url解析
from bs4 import BeautifulSoup #以正则匹配html
import datetime
import re

# 数值处理
def toInt(str):
    if 'w' in str or '万' in str:
        num = float(re.findall(r"\d+\.?\d*", str)[0])
        num = int(num * 10000)
    else:
        num = int(re.findall(r"\d+\.?\d*", str)[0])
    return num



# 用户实体类
class user():
    # 构造函数
    def __init__(self, id):
        # 拼接url
        self.urlVideo = 'https://chushou.tv/u/' + str(id) + '-2.htm'
        self.urlNews = 'https://chushou.tv/u/timeline/down.htm?uid=' + str(id) + '&pageSize=20'
        self.id = id
        self.name = ''
        self.fanNum = 0
        self.followNum = 0
        self.giftNum = 0
        # [标题，发布时间，播放，评论，礼物]
        self.videoList = []
        # [内容，发布时间，点赞，评论]
        self.newsList = []
        self.spider()
        # self.date = datetime.datetime.now().strftime('%Y-%m-%d')
        # self.time = datetime.datetime.now().strftime('%H:%M:%S')
        # self.week = datetime.datetime.now().isocalendar()

    # 爬虫主函数
    def spider(self):
        header = {
            'Cookie': 'login_sid_t=a7a5a917967eb55d43064ec167a7915e; cross_origin_proto=SSL; YF-Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; YF-V5-G0=cd5d86283b86b0d506628aedd6f8896e; YF-Page-G0=8fee13afa53da91ff99fc89cc7829b07; _s_tentry=passport.weibo.com; Apache=5372054505778.079.1537256027439; SINAGLOBAL=5372054505778.079.1537256027439; ULV=1537256027450:1:1:1:5372054505778.079.1537256027439:; WBtopGlobal_register_version=9744cb1b8d390b27; SUHB=0BL5mukVaXtbyM; UOR=,,login.sina.com.cn; wb_view_log_2521076772=1920*10801; sensorsdata_is_new_user=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22165eba3eb27616-00509dc9b2e035-2c7c294a-326000-165eba3eb291052%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; UM_distinctid=165eba3ec9941e-070df1d582a4bc-2c7c294a-4f970-165eba3ec9a8d5; SUB=_2AkMs_DkudcPxrAFUmvkVy23la49H-jyfKVDYAn7uJhMyAxgv7noAqSVutBF-XDHx2lUPxLzOqkB-dEaoV06LyvCf; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WhBYPf4Y6gFN8qyYiSdVnGO5JpV2c9adspaUfvNIg4.Bh2ESb4odcXt; wb_view_log=1920*10801',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        }  # 模拟浏览器访问url

        # 抓视频页
        request = urllib.request.Request(self.urlVideo, headers=header)
        response = urllib.request.urlopen(request).read()
        html =str(response,'utf-8')
        soup = BeautifulSoup(html, "lxml")
        # print(soup)

        # 用户基本信息
        self.name = soup.find('span', attrs={'class': 'nickname'}).string
        self.fanNum = toInt(soup.find_all('span', attrs={'class': 'count_text'})[0].string)
        self.followNum = toInt(soup.find_all('span', attrs={'class': 'count_text'})[1].string)
        self.giftNum = toInt(str(soup.find('span', attrs={'class': 'gift_num'})))
        # print(self.name)
        # print(self.fanNum)
        # print(self.followNum)
        # print(self.giftNum)

        # 处理视频信息
        videoCode= soup.find_all('div', attrs={'class': 'liveOne'})
        for i in range(len(videoCode)):
            title = videoCode[i].find('a', attrs={'class': 'videoName'}).string
            publishTime = videoCode[i].find('span', attrs={'class': 'createtime'}).string
            playNum = toInt(videoCode[i].find_all('span', attrs={'class': 'liveCount'})[0].string)
            giftNum = toInt(videoCode[i].find_all('span', attrs={'class': 'liveCount'})[2].string)
            commentNum = toInt(videoCode[i].find_all('span', attrs={'class': 'liveCount'})[1].string)
            self.videoList.append([title, publishTime, playNum, giftNum, commentNum])
            # print(self.videoList[i])

        # 抓动态页
        request = urllib.request.Request(self.urlNews, headers=header)
        response = urllib.request.urlopen(request).read()
        html = str(response, 'utf-8')
        soup = BeautifulSoup(html, "lxml")
        # print(soup)

        # 处理动态信息
        newsCode = soup.find_all('div', attrs={'class': 'timelineCommend'})
        for i in range(len(newsCode)):
            content = newsCode[i].find('div', attrs={'class': 'content'}).string.strip()
            publishTime = newsCode[i].find('div', attrs={'class': 'timebox'}).string.replace('发布时间：','')
            likeNum = toInt(newsCode[i].find('span', attrs={'class': 'linetext'}).string)
            commentNum = toInt(newsCode[i].find_all('span', attrs={'class': 'text'})[2].string)
            self.newsList.append([content, publishTime, likeNum, commentNum])
            # print(self.newsList[i])

# 列表类
class chuShouList():
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
            # 用户ID、名称、粉丝、关注、礼物
            userInfo.append(
                [self.user[i].id, self.user[i].name, self.user[i].fanNum,
                 self.user[i].followNum, self.user[i].giftNum]
            )
        # for i in range(len(userInfo)):
        #     print(userInfo[i])
        return userInfo

    # 外部视频信息接口
    def getVideoInfo(self):
        videoInfo = []
        for i in range(len(self.user)):
            for j in range(len(self.user[i].videoList)):
                # 用户ID、名称、[标题，发布时间，播放，评论，礼物]
                videoInfo.append(
                    [self.user[i].id, self.user[i].name, self.user[i].videoList[j][0], self.user[i].videoList[j][1],
                     self.user[i].videoList[j][2], self.user[i].videoList[j][3], self.user[i].videoList[j][4]]
                )
        # for i in range(len(videoInfo)):
        #     print(videoInfo[i])
        return videoInfo

    # 外部动态信息接口
    def getNewsInfo(self):
        newsInfo = []
        for i in range(len(self.user)):
            for j in range(len(self.user[i].newsList)):
                # 用户ID、名称、[内容，发布时间，点赞，评论]
                newsInfo.append(
                    [self.user[i].id, self.user[i].name, self.user[i].newsList[j][0], self.user[i].newsList[j][1],
                     self.user[i].newsList[j][2], self.user[i].newsList[j][3]]
                )
        # for i in range(len(newsInfo)):
        #   print(newsInfo[i])
        return newsInfo


# idPool = ['1238526270','1238174523']
# chuShouList = chuShouList(idPool)
# chuShouList.getUserInfo()
# chuShouList.getVideoInfo()
# chuShouList.getNewsInfo()

