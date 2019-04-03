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
            'Cookie': 'login_sid_t=a7a5a917967eb55d43064ec167a7915e; cross_origin_proto=SSL; YF-Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; YF-V5-G0=cd5d86283b86b0d506628aedd6f8896e; YF-Page-G0=8fee13afa53da91ff99fc89cc7829b07; _s_tentry=passport.weibo.com; Apache=5372054505778.079.1537256027439; SINAGLOBAL=5372054505778.079.1537256027439; ULV=1537256027450:1:1:1:5372054505778.079.1537256027439:; WBtopGlobal_register_version=9744cb1b8d390b27; SUHB=0BL5mukVaXtbyM; UOR=,,login.sina.com.cn; wb_view_log_2521076772=1920*10801; sensorsdata_is_new_user=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22165eba3eb27616-00509dc9b2e035-2c7c294a-326000-165eba3eb291052%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; UM_distinctid=165eba3ec9941e-070df1d582a4bc-2c7c294a-4f970-165eba3ec9a8d5; SUB=_2AkMs_DkudcPxrAFUmvkVy23la49H-jyfKVDYAn7uJhMyAxgv7noAqSVutBF-XDHx2lUPxLzOqkB-dEaoV06LyvCf; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WhBYPf4Y6gFN8qyYiSdVnGO5JpV2c9adspaUfvNIg4.Bh2ESb4odcXt; wb_view_log=1920*10801',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
        }  # 模拟浏览器访问url

        request = urllib.request.Request(self.url, headers=header)

        response = urllib.request.urlopen(request).read()
        html =str(response,'utf-8')
        soup = BeautifulSoup(html, "lxml")
        # print(soup)
        # 用户基本信息
        self.name = soup.find('div',attrs={'class':'user-name'}).contents[0].string.strip()
        self.fanNum = int(soup.find('li', attrs={'class': 'snum'}).get('title').replace(',', ''))
        self.videoPlayNumAll = int(soup.find('li', attrs={'class': 'vnum'}).get('title').replace(',',''))
        self.videoNum = toInt(soup.find('div', attrs={'class': 'title'}).find('span').string.strip())
        # print(soup.find('div', attrs={'class': 'title'}).find('span'))

        # 处理视频信息
        # 视频标题、发布时间、播放量
        videoCode= soup.find_all('div', attrs={'class': 'v-meta'})
        # print(toInt(videoCode[0].find('span', attrs={'class': 'v-num'}).string))
        for i in range(len(videoCode)):
            title =videoCode[i].find('div', attrs={'class': 'v-meta-title'}).contents[0].get('title')
            publishTime = videoCode[i].find('span', attrs={'class': 'v-publishtime'}).string
            playNum = toInt(videoCode[i].find('span', attrs={'class': 'v-num'}).string)
            self.videoList.append([title,publishTime,playNum,])


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

# idPool = ['http://i.youku.com/i/UMzE2OTY2NjUy/videos', 'https://i.youku.com/i/UNDM0NTE0MzMy/videos','https://i.youku.com/i/UNDY1ODA3MzY2OA==/videos']
# youKuList = youKuList(idPool)
# youKuList.getUserInfo()
# youKuList.getVideoInfo()

