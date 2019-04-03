#-*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import re
import time
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

def nga(userId=[]):
    
    print('开始抓取NGA文章数据：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('抓取最近35条用户动态')

    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Cookie':'__guid=16065253.2572202618274932000.1536548584622.0288; UM_distinctid=165c16ec3a51b5-09856630e25112-5d4e211f-100200-165c16ec3a619b; taihe=dd2957e86dda39b9dc255fc7ad833da1; ngaPassportUid=43304202; ngaPassportUrlencodedUname=%25B7%25C9%25CC%25EC%25D6%25EDvivi; ngaPassportCid=Z8ls6ol4ng76tjnshpubr6c897d1k1uc6oluickn; CNZZDATA1262314555=238781265-1536548056-http%253A%252F%2F%252Fbbs.nga.cn%252%252F%7C1537425468; ngacn0comUserInfo=%25B7%25C9%25CC%25EC%25D6%25EDvivi%09%25E9%25A3%259E%25E5%25A4%25A9%25E7%258C%25AAvivi%0939%0939%09%0910%090%094%090%090%09; ngacn0comUserInfoCheck=b9d06e66d33df822f4c2d21b428bac07; ngacn0comInfoCheckTime=1537520488; lastvisit=1537520563; lastpath=/h=/thread.php?aut?authorid=42721247; monitor_count=12; bbsmisccookies=%7B%22insad_refreshid%22%3A%7B0%3A%22/153741239727136%22%2C1%3A1538125284%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-42%2C1%3A1537549248%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1537549248%7D%7D; CNZZDATA30043604=cnzz_eid%3D118350130-1536544535-http%253A%252F%2F%252Fbbs.ngacn.cc%252%252F%26ntime%3D1537517074; CNZZDATA30039253=cnzz_eid%3D1177591156-1536545359-http%253A%252F%2F%252Fbbs.ngacn.cc%252%252F%26ntime%3D1537520261; taihe_session=37308d2fa877a66507f0fb67ffc39167; Hm_lvt_5adc78329e14807f050ce131992ae69b=1537162198,1537331325,1537425343,1537520487; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1537520560',
    #'Cookie': 'UM_distinctid=165f15b8dac1dd-0f547c99ac0f7f-8383268-1fa400-165f15b8dad9e3; taihe=956a2609276d37ff19a386e0147bee8d; CNZZDATA1262314555=1351202106-1537352274-http%253A%252F%252Fbbs.nga.cn%252F%7C1537409262; Hm_lvt_5adc78329e14807f050ce131992ae69b=1537352633,1537413517,1537519869; ngacn0comUserInfo=%25CB%25E6%25B1%25E3%25D7%25A2%25B2%25E1%25B8%25F6%25C3%25FB%25D7%25D6%09%25E9%259A%258F%25E4%25BE%25BF%25E6%25B3%25A8%25E5%2586%258C%25E4%25B8%25AA%25E5%2590%258D%25E5%25AD%2597%0939%0939%09%0910%090%090%090%090%09; ngaPassportUid=25826632; ngaPassportUrlencodedUname=%25CB%25E6%25B1%25E3%25D7%25A2%25B2%25E1%25B8%25F6%25C3%25FB%25D7%25D6; ngaPassportCid=Z8m1non522rfg73jcheaj3o6u95pb55utlc5h63j; CNZZDATA30039253=cnzz_eid%3D864576377-1537347456-null%26ntime%3D1537520261; CNZZDATA1256638869=1002817106-1537517327-http%253A%252F%252Fbbs.nga.cn%252F%7C1537517327; lastpath=/thread.php?authorid=15169320; lastvisit=1537522538; ngacn0comUserInfoCheck=b474fb8ea954718afd0c9d4143cac250; ngacn0comInfoCheckTime=1537522538; bbsmisccookies=%7B%22insad_refreshid%22%3A%7B0%3A%22/153741239727136%22%2C1%3A1538124668%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-30%2C1%3A1537549217%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1537549217%7D%7D; taihe_session=da47cbbcb1d84b51bc0cf3f860c2199b; CNZZDATA30043604=cnzz_eid%3D840379136-1537349995-null%26ntime%3D1537522474; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1537522541',
    'Host': 'bbs.nga.cn',
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive'
    
    
    }#模拟浏览器访问url
    
    #获取所有文章列表
    
    i = 0
    resData = []
    while i < len(userId):
        #time.sleep(5)
        page = 1
        while page<=1: #抓取1页35条帖子
            userUrl = 'http://bbs.nga.cn/thread.php?authorid='+str(userId[i]) #访问博主信息
            userRequest = urllib.request.Request(userUrl,headers=header)
            userResponse = urllib.request.urlopen(userRequest).read()
            tag = SoupStrainer('table')#只解析所有内容中给定条件的内容，节省内存和时间
            soup = BeautifulSoup(userResponse,"lxml",parse_only=tag)
            reply = soup.find_all('a',attrs={'class':'replies'})
            topic = soup.find_all('a',attrs={'title':None,'id':True,'href':True})
            topicTime = soup.find_all('span',attrs={'class':'silver postdate'})#attrs['title']
            j = 0
            while j<len(reply):
                resData_ = []
                resData_.extend([userId[i],topic[2*j].string,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(topicTime[j].string))),reply[j].string])
                resData.append(resData_)
                j+=1
            page+=1
        i+=1

    return resData








