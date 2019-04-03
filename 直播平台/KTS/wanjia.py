#coding=utf-8

import urllib.request
import urllib.parse
import re
import time
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

def wanjia(userId=[]):
    
    print('开始抓取玩加文章数据：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('抓取最近20条用户动态')

    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }#模拟浏览器访问url
    
    #获取所有文章列表
    urls = []
    i = 0
    while i < len(userId):
        #time.sleep(5)
               
        userUrl = 'https://www.wanplus.com/people/'+str(userId[i]) #访问博主信息
        userRequest = urllib.request.Request(userUrl,headers=header)
        userResponse = urllib.request.urlopen(userRequest).read()
        tag = SoupStrainer('div',attrs={'class':'note-post-top'})#只解析所有内容中给定条件的内容，节省内存和时间
        soup = BeautifulSoup(userResponse,"lxml",parse_only=tag)
        
        values = soup.find_all('span') #判断用户动态是发表文章还是评论文章
        value=[]
        for v in values:
            value.append(v.string)
        #print(value)
        hrefs = soup.find_all('a') #获取所有url
        href=[]
        for h in hrefs:
            href.append(h.attrs['href'])
        j = 0
        #print(href)
        while j<len(value):
            if value[j].strip()=='发表了文章':#.strip()将字符串左右侧空格删除
                urls.append([userId[i],href[j]])

            j+=1
        i+=1
    #print(urls)

    #读取文章数据
    
    i = 0
    while i < len(urls):
        try:
            topicUrl = 'https://www.wanplus.com'+urls[i][1]
            topicRequest = urllib.request.Request(topicUrl,headers=header)
            topicResponse = urllib.request.urlopen(topicRequest).read()
            soup = BeautifulSoup(topicResponse,"lxml")
            name = soup.find('img',attrs={'onerror':True}).attrs['alt']
            title = soup.find('h1').string
            topicTime = soup.find('span','com-time').string
            read = soup.find('em','com-num m-hide').string
            favorite = soup.find('div','com-zan').span.string
            #pattern = re.compile(r'[(](.*?)[)]')
            com = re.findall(r'[(](.*?)[)]',soup.find('h3').string)#使用正则表达式提取数字
            try:
                com = com[0]
            except:
                com = 0
            #print(name,title,topicTime,read,favorite,com)
            urls[i].extend([name,title,topicTime,read,favorite,com])

            i+=1
        except:
            i+=1
        
    #print(urls)

    return urls



