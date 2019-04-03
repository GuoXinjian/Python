import urllib.request #url请求
import urllib.parse #url解析
from bs4 import BeautifulSoup #以正则匹配html
import datetime
import time
import json
import re

# 数值处理
def toInt(str):
    if 'w' in str or '万' in str:
        num = float(re.findall(r"\d+\.?\d*", str)[0])
        num = int(num * 10000)
    else:
        num = int(re.findall(r"\d+\.?\d*", str)[0])
    return num

# 时间戳处理
def toDatetime(timeStamp):
    # 转换成localtime
    time_local = time.localtime(int(timeStamp))
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt  # 2013--10--10 15:40:00

# 快手用户实体类
class user():
    # 构造函数
    def __init__(self, id):

        # 拼接url
        self.urlUser = 'https://www.ixigua.com/c/user/'+ str(id)
        self.urlVideo = 'https://www.ixigua.com/c/user/article/?user_id=' + str(id) + '&max_behot_time=0&max_repin_time=0&count=30&page_type=0'
        self.id = id
        self.name = ''
        self.description = ''
        self.fanNum = 0
        self.followNum = 0
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

        request = urllib.request.Request(self.urlUser, headers=header)
        response = urllib.request.urlopen(request).read()
        html =str(response,'utf-8')
        # print(html)

        # 用户基本信息
        self.name = re.findall(r'name: \'(.*?)\',',html, re.S)[0]
        self.fanNum = int(re.findall(r'followedNum: (.*?)}',html, re.S)[0])
        self.followNum = int(re.findall(r'followingNum: (.*?),',html, re.S)[0])

        request = urllib.request.Request(self.urlVideo, headers=header)
        response = urllib.request.urlopen(request).read()
        html = str(response, 'utf-8')

        # 处理视频信息
        videoJson= str(json.loads(html))
        titleLsit = re.findall(r'\'title\': \'(.*?)\',',videoJson, re.S)
        # print(len(titleLsit),titleLsit)
        publishTimeList = re.findall(r'\'behot_time\': (.*?),',videoJson, re.S)
        # print(len(publishTimeList), publishTimeList)
        playNumList = re.findall(r'\'video_watch_count\': (.*?)}',videoJson, re.S)
        # print(len(playNumList), playNumList)
        commentNumList = re.findall(r'\'comments_count\': (.*?),',videoJson, re.S)
        # print(len(commentNumList), commentNumList)
        for i in range(len(titleLsit)):
            self.videoList.append([titleLsit[i], toDatetime(publishTimeList[i]), toInt(playNumList[i]), toInt(commentNumList[i])])
            # print(self.videoList[i])

# 列表类
class xiGuaList():
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
            # 用户ID、名称、粉丝、关注
            userInfo.append(
                [self.user[i].id, self.user[i].name, self.user[i].fanNum,
                 self.user[i].followNum]
            )
        # for i in range(len(userInfo)):
        #         #     print(userInfo[i])
        return userInfo

    # 外部视频信息接口
    def getVideoInfo(self):
        videoInfo = []
        for i in range(len(self.user)):
            for j in range(len(self.user[i].videoList)):
                # 用户ID、名称、标题、发布时间、 播放、评论
                videoInfo.append(
                    [self.user[i].id, self.user[i].name, self.user[i].videoList[j][0], self.user[i].videoList[j][1],
                     self.user[i].videoList[j][2], self.user[i].videoList[j][3]]
                )
        # for i in range(len(videoInfo)):
        #     print(videoInfo[i])
        return videoInfo



# idPool = ['67870829304']
# xiGuaList = xiGuaList(idPool)
# xiGuaList.getUserInfo()
# xiGuaList.getVideoInfo()

