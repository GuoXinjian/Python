import urllib.request #url请求
import urllib.parse #url解析
from bs4 import BeautifulSoup #以正则匹配html
import time
import datetime
import re
import json
from selenium import webdriver
import os

filePath = os.path.dirname(__file__)
chromedriver = filePath + "/chromedriver.exe"
phantomjs = filePath + "/phantomjs.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
# 用户实体类
class user():
    # 构造函数
    def __init__(self, id):
        self.driver = webdriver.Chrome(chromedriver)
        self.url = 'https://www.toutiao.com/c/user/'+ id
        self.name = ''
        self.followNum = 0
        self.fanNum = 0
        self.artiInfo = []
        self.videoNum = 0
        self.spider()

    # 爬虫主函数
    def spider(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        # 判断网页是否正常打开
        timeFlag = 0
        while (len(self.driver.find_elements_by_class_name("comment")) <= 0):
            if(timeFlag > 5):
                self.driver.refresh()
                timeFlag = 0
            time.sleep(1)
            timeFlag += 1

        # 用户id
        self.name = self.driver.find_elements_by_class_name("name")[1].text
        # print(self.name)
        # 关注、粉丝
        self.followNum = self.driver.find_elements_by_class_name("y-number")[0].text
        self.fanNum = self.driver.find_elements_by_class_name("y-number")[1].text
        # print(self.followNum)
        # print(self.fanNum)
        # 类型 标题 发布时间 播放/阅读 评论
        if(len(self.driver.find_elements_by_class_name("item")) == 20):
            # 下拉到页面底部
            js = "var q=document.documentElement.scrollTop=100000"
            self.driver.execute_script(js)
            time.sleep(5)
        for i in range(len(self.driver.find_elements_by_class_name("item"))):
            if ('播放' in self.driver.find_elements_by_class_name("item")[i].find_elements_by_class_name("lbtn")[0].text):
                type = '视频'
                self.videoNum += 1
            else:
                type = '文章'
            # 筛选掉“置顶”
            if(self.driver.find_elements_by_class_name("item")[i].find_elements_by_class_name("lbtn")[0].text == '置顶'):
                self.artiInfo.append(
                    [type, self.driver.find_elements_by_class_name("item")[i].find_element_by_class_name("title-box").text,
                     toInt(self.driver.find_elements_by_class_name("item")[i].find_elements_by_class_name("lbtn")[1].text),
                     toInt(self.driver.find_elements_by_class_name("item")[i].find_elements_by_class_name("lbtn")[2].text),
                     self.driver.find_elements_by_class_name("item")[i].find_elements_by_class_name("lbtn")[3].text.replace('⋅ ','')])
            else:
                self.artiInfo.append(
                    [type,
                     self.driver.find_elements_by_class_name("item")[i].find_element_by_class_name("title-box").text,
                     toInt(self.driver.find_elements_by_class_name("item")[i].find_elements_by_class_name("lbtn")[
                               0].text),
                     toInt(self.driver.find_elements_by_class_name("item")[i].find_elements_by_class_name("lbtn")[
                               1].text),
                     self.driver.find_elements_by_class_name("item")[i].find_elements_by_class_name("lbtn")[2].text.replace('⋅ ','')])
            # print(self.artiInfo[i])
        self.driver.quit()

# 列表类
class touTiaoList():
    def __init__(self, idPool):
        self.idPool = []
        self.user = []
        for i in range(len(idPool)):
            self.idPool.append(idPool[i])
        for i in range(len(self.idPool)):
            # print(self.idPool[i])
            self.user.append(user(self.idPool[i]))

    # 外部用户信息接口
    def getUserInfo(self):
        userInfo = []
        for i in range(len(self.user)):
            # 用户ID、关注数、粉丝量、视频数、图文数
            userInfo.append(
                [self.user[i].name, self.user[i].fanNum,
                 self.user[i].followNum, self.user[i].videoNum, len(self.user[i].artiInfo) - self.user[i].videoNum]
            )
        # for i in range(len(userInfo)):
        #     print(userInfo[i])
        return userInfo

    # 外部视频信息接口
    def getArtiInfo(self):
        artiInfo = []
        for i in range(len(self.user)):
            for j in range(len(self.user[i].artiInfo)):
                # 用户ID 类型 标题 发布时间 播放/阅读 评论
                artiInfo.append(
                    [self.user[i].name, self.user[i].artiInfo[j][0], self.user[i].artiInfo[j][1],
                     self.user[i].artiInfo[j][2], self.user[i].artiInfo[j][3], self.user[i].artiInfo[j][4]]
                )
        # for i in range(len(artiInfo)):
        #     print(artiInfo[i])
        return artiInfo


# 数值处理
def toInt(str):
    if 'w' in str or '万' in str:
        num = float(re.findall(r"\d+\.?\d*", str)[0])
        num = int(num * 10000)
    else:
        num = int(re.findall(r"\d+", str)[0])
    return num



# idPool = ['104204887690/#mid=1610834732822536','3640419564/#mid=3650447777']
# id = '3640419564/#mid=3650447777'
# touTiaoList = touTiaoList(idPool)
# touTiaoList.getUserInfo()
# touTiaoList.getArtiInfo()

# as/cp解密
# def get_ASCP():
#     t = int(math.floor(time.time()))
#     e = hex(t).upper()[2:]
#     m = hashlib.md5()
#     m.update(str(t).encode(encoding='utf-8'))
#     i = m.hexdigest().upper()
#
#     if len(e) != 8:
#         AS = '479BB4B7254C150'
#         CP = '7E0AC8874BB0985'
#         return AS, CP
#     n = i[0:5]
#     a = i[-5:]
#     s = ''
#     r = ''
#     for o in range(5):
#         s += n[o] + e[o]
#         r += e[o + 3] + a[o]
#
#     AS = 'AL' + s + e[-3:]
#     CP = e[0:3] + r + 'E1'
#     # print("AS:"+ AS,"CP:" + CP)
#     return AS, CP
