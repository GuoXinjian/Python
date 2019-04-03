#coding=utf-8

import urllib.request
import urllib.parse
import re
import time
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

def toInt(str):
    if 'w' in str or '万' in str:
        num = float(re.findall(r"\d+\.?\d*", str)[0])
        num = int(num * 10000)
    else:
        num = int(re.findall(r"\d+\.?\d*", str)[0])
    return num

def weishi(userId=[]):
    
    print('开始抓取weishi数据：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print('抓取最近9条用户动态')

    header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
    #'Cookie':'_cnzz_CV30020080=buzi_cookie%7C81a3e35e.0e02.b115.81b8.d46dc33e7230%7C-1; PHPSESSID=cajqno4piuaq5r2217cqqfufd1; _dacevid3=81a3e35e.0e02.b115.81b8.d46dc33e7230; _HUPUSSOID=490215f7-2a67-4577-a770-bfcae1da1527; _CLT=00376064be821b71351c003dda774e37; u=39242614|5Zmi6YOt6ICB5biI|abe1|a115c0312220d21cf725929f409f1768|2220d21cf725929f|aHVwdV9jYzdjMzM1ZTI5MWVhMzcx; us=4307bd5e99e50d526e4950811e21a777f202801e35da060419cc01faf9cc0927ad96cea784d3801aac96afe47960cec67b61e429b777a2207387b6b6e9119523; ua=102545712; __dacevst=3b1e47ab.59a324d1|1538187482308',
    #'Cookie': 'UM_distinctid=165f15b8dac1dd-0f547c99ac0f7f-8383268-1fa400-165f15b8dad9e3; taihe=956a2609276d37ff19a386e0147bee8d; CNZZDATA1262314555=1351202106-1537352274-http%253A%252F%252Fbbs.nga.cn%252F%7C1537409262; Hm_lvt_5adc78329e14807f050ce131992ae69b=1537352633,1537413517,1537519869; ngacn0comUserInfo=%25CB%25E6%25B1%25E3%25D7%25A2%25B2%25E1%25B8%25F6%25C3%25FB%25D7%25D6%09%25E9%259A%258F%25E4%25BE%25BF%25E6%25B3%25A8%25E5%2586%258C%25E4%25B8%25AA%25E5%2590%258D%25E5%25AD%2597%0939%0939%09%0910%090%090%090%090%09; ngaPassportUid=25826632; ngaPassportUrlencodedUname=%25CB%25E6%25B1%25E3%25D7%25A2%25B2%25E1%25B8%25F6%25C3%25FB%25D7%25D6; ngaPassportCid=Z8m1non522rfg73jcheaj3o6u95pb55utlc5h63j; CNZZDATA30039253=cnzz_eid%3D864576377-1537347456-null%26ntime%3D1537520261; CNZZDATA1256638869=1002817106-1537517327-http%253A%252F%252Fbbs.nga.cn%252F%7C1537517327; lastpath=/thread.php?authorid=15169320; lastvisit=1537522538; ngacn0comUserInfoCheck=b474fb8ea954718afd0c9d4143cac250; ngacn0comInfoCheckTime=1537522538; bbsmisccookies=%7B%22insad_refreshid%22%3A%7B0%3A%22/153741239727136%22%2C1%3A1538124668%7D%2C%22pv_count_for_insad%22%3A%7B0%3A-30%2C1%3A1537549217%7D%2C%22insad_views%22%3A%7B0%3A1%2C1%3A1537549217%7D%7D; taihe_session=da47cbbcb1d84b51bc0cf3f860c2199b; CNZZDATA30043604=cnzz_eid%3D840379136-1537349995-null%26ntime%3D1537522474; Hm_lpvt_5adc78329e14807f050ce131992ae69b=1537522541',
    #'Host': 'bbs.nga.cn',
    #'Upgrade-Insecure-Requests': '1',
    #'Connection': 'keep-alive'
    
    
    }#模拟浏览器访问url
    
    #获取所有文章列表
    
    i = 0
    resData1 = []
    resData2 = []
    while i < len(userId):
        #time.sleep(5)
    
        userUrl = 'https://h5.weishi.qq.com/weishi/personal/'+str(userId[i]) #访问博主信息
        userRequest = urllib.request.Request(userUrl,headers=header)
        userResponse = urllib.request.urlopen(userRequest).read()
        #print(userResponse)
        tag1 = SoupStrainer('div',{'class':'infor'})#只解析所有内容中给定条件的内容，节省内存和时间
        soup1 = BeautifulSoup(userResponse,"lxml",parse_only=tag1)

        name = soup1.find_all('span',attrs={'class':'name'})[0].string
        desc = soup1.find_all('p',attrs={'class':'description'})[0].string
        fans = toInt(soup1.find_all('span',attrs={'class':'num j-numeric-fans'})[0].string)
        follow = toInt(soup1.find_all('span',attrs={'class':'num j-numeric-interest'})[0].string)
        praise = toInt(soup1.find_all('span',attrs={'class':'num j-numeric-receivepraise'})[0].string)
        #print(soup)
        resData1.append([userId[i],name,desc,fans,follow,praise])


        tag2 = SoupStrainer('li')
        soup2 = BeautifulSoup(userResponse,'lxml',parse_only=tag2)

        videoId = soup2.find_all('li',{'class':'figure-item j-figure-item'})
        play = soup2.find_all('b')
        j = 0
        while j<len(videoId):
            resData2.append([userId[i],videoId[j].attrs['data-id'],toInt(play[j].string)])
            j+=1
        
        i+=1

    return resData1,resData2


#weishi(['1526460070936802'])





