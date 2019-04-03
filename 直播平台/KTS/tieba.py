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
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }#模拟浏览器访问url
    
    #获取所有文章列表
    urls=[]
    res = []
    userId_=[]
    i = 0
    while i < len(userId):
        #time.sleep(5)
        userId_ = urllib.parse.quote(userId[i],'utf-8')  #将博主名称编码为url
        userUrl = 'http://tieba.baidu.com/home/main?un='+userId_ #访问博主信息
        userRequest = urllib.request.Request(userUrl,headers=header)
        userResponse = urllib.request.urlopen(userRequest).read()
        tag1 = SoupStrainer('a',attrs={'class':'title'})#只解析所有内容中给定条件的内容，节省内存和时间
        soup1 = BeautifulSoup(userResponse,"lxml",parse_only=tag1)
        topic = soup1.find_all('a')
        tag2 = SoupStrainer('div',attrs={'class':'n_post_time'})#只解析所有内容中给定条件的内容，节省内存和时间
        soup2 = BeautifulSoup(userResponse,"lxml",parse_only=tag2)
        postTime = soup2.find_all('div')
        j = 0
        while j<len(topic):
            urls.append(topic[j].attrs['href'])
            res.append([userId[i],topic[j].string,postTime[j].string])
            j+=1
        i+=1
    #print(urls)
    #print(res)

    
    i=0
    while i < len(urls):
        topicUrl = 'https://tieba.baidu.com'+urls[i]
        topicRequest = urllib.request.Request(topicUrl,headers=header)
        topicResponse = urllib.request.urlopen(topicRequest).read()
        tag = SoupStrainer('li',attrs={'class':'l_reply_num'})
        soup = BeautifulSoup(topicResponse,'lxml',parse_only=tag)
        reply = soup.find_all('span')
        res[i].append(reply[0].string)
        i+=1

    #print(res)
    return res

