import urllib.request #url请求
import urllib.parse #url解析
from bs4 import BeautifulSoup #以正则匹配html
import excel #自己做的操作EXCEL类
import datetime 
import time
import json #json解析



while True:#计时器
    while True:
        now = datetime.datetime.now()
        if now.minute == 0: #当分钟==0时，执行程序
            break
        time.sleep(20) #过20秒再检查一下

        #获取sheet'weibo'的urls
        urls = excel.loadUrl('weibo')
        print(urls)

        i = 0
        while i < len(urls):
            header = {
            'Cookie': 'login_sid_t=a7a5a917967eb55d43064ec167a7915e; cross_origin_proto=SSL; YF-Ugrow-G0=9642b0b34b4c0d569ed7a372f8823a8e; YF-V5-G0=cd5d86283b86b0d506628aedd6f8896e; YF-Page-G0=8fee13afa53da91ff99fc89cc7829b07; _s_tentry=passport.weibo.com; Apache=5372054505778.079.1537256027439; SINAGLOBAL=5372054505778.079.1537256027439; ULV=1537256027450:1:1:1:5372054505778.079.1537256027439:; WBtopGlobal_register_version=9744cb1b8d390b27; SUHB=0BL5mukVaXtbyM; UOR=,,login.sina.com.cn; wb_view_log_2521076772=1920*10801; sensorsdata_is_new_user=true; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22165eba3eb27616-00509dc9b2e035-2c7c294a-326000-165eba3eb291052%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; UM_distinctid=165eba3ec9941e-070df1d582a4bc-2c7c294a-4f970-165eba3ec9a8d5; SUB=_2AkMs_DkudcPxrAFUmvkVy23la49H-jyfKVDYAn7uJhMyAxgv7noAqSVutBF-XDHx2lUPxLzOqkB-dEaoV06LyvCf; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WhBYPf4Y6gFN8qyYiSdVnGO5JpV2c9adspaUfvNIg4.Bh2ESb4odcXt; wb_view_log=1920*10801',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
            }#模拟浏览器访问url
            videoRequest = urllib.request.Request(urls[i],headers=header)
            vidoeResponse = urllib.request.urlopen(videoRequest).read()
            #print(vidoeResponse)

            soup = BeautifulSoup(vidoeResponse,"lxml")

            num = soup.find_all('em',attrs={'class':None,'node-type':None})
            broadTime = soup.find_all('div',attrs={'class':'broad_time W_f12'})
            title = soup.find_all('div',attrs={'class':'info_txt W_f14'})
            #print(num)
            data = [urls[i][-21:],urls[i],time.strftime('%Y-%m-%d %H', time.localtime(time.time())),
            num[0].string,num[1].string,num[2].string,num[3].string,broadTime[0].string,title[0].string]
            #print(data)
            excel.appendData(data)
            i+=1
        excel.saveData()

        #获取sheet'bilibili'的urls
        urls = excel.loadUrl('bilibili')
        urlHead = 'https://api.bilibili.com/x/web-interface/view?aid=' 
        i = 0

        while i< len(urls):
            header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
            }#模拟浏览器访问url
            videoRequest = urllib.request.Request((urlHead+urls[i][-8:]),headers=header)
            vidoeResponse = urllib.request.urlopen(videoRequest).read()
            #print(vidoeResponse)
            bilibiliData = json.loads(vidoeResponse)
            data = [urls[i][-10:],urls[i],time.strftime('%Y-%m-%d %H', time.localtime(time.time())),
            bilibiliData['data']['stat']['view'],bilibiliData['data']['stat']['share'],bilibiliData['data']['stat']['reply'],bilibiliData['data']['stat']['like'],
            time.strftime("%Y-%m-%d %H",time.localtime(bilibiliData['data']['ctime'])),bilibiliData['data']['title']]
            excel.appendData(data)
            i+=1
        excel.saveData()
            



        time.sleep(30)
        