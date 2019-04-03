# coding=utf-8

import urllib.request
import urllib.parse
import re
import time
import sys
from bs4 import BeautifulSoup
from bs4 import SoupStrainer



def tieba(userId=[]):
    
    print('开始抓取贴吧文章数据：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('抓取最近20条用户动态')

    header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36'
    }#模拟手机浏览器访问url
    
    #获取所有文章列表

    res = []
    userId_=[]
    i = 0
    while i < len(userId):
        #time.sleep(5)
        userId_ = urllib.parse.quote(userId[i],'utf-8')  #将博主名称编码为url
        userUrl = 'http://tieba.baidu.com/home/main?un='+userId_ #访问博主信息
        #print(userUrl)
        userRequest = urllib.request.Request(userUrl,headers=header)
        #print(userRequest)
        userResponse = urllib.request.urlopen(userRequest).read()
        #print(userResponse)
        tag = SoupStrainer('li')#只解析所有内容中给定条件的内容，节省内存和时间
        soup = BeautifulSoup(userResponse,"lxml",parse_only=tag)
        #print(soup)
        topic = soup.find_all('span',{'class':'post_list_item_title'})
        postTime= soup.find_all('span',{'class':'post_list_item_info_time'})
        reply = soup.find_all('span',{'class':'post_item_info_reply_icon'})
        #print(topic)
        #print(postTime)
        #print(reply)
        j = 0
        while j<len(topic):
            topic_ = re.sub("<[^>]+>","",str(topic[j]))
            res.append([userId[i],topic_,postTime[j].string,reply[j].string])
            j+=1
        i+=1
    #print(urls)
    #print(res)
    return res

#tieba(['VSPN_KPL联赛'])