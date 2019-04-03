import urllib.request #url请求
import urllib.parse #url解析
import re
import time
import json
#7fbed6756baeba7fe370ba49c9e883e0
def toInt(str):
    if 'w' in str or '万' in str:
        num = float(re.findall(r"\d+\.?\d*", str)[0])
        num = int(num * 10000)
    else:
        num = int(re.findall(r"\d+\.?\d*", str)[0])
    return num

def v_qq(userId=[]):
    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
    }#模拟浏览器访问url
    

    i = 0
    res = []
    while i < len(userId):
        #time.sleep(5)
        page=1
        while page<=1:#抓1页的数据 每页30个视频
            userUrl = 'http://c.v.qq.com/vchannelinfo?otype=json&qm=1&num=30&uin=' + str(userId[i])+'&pagenum='+str(page) #访问博主状态信息
            # print(userUrl)
            userRequest = urllib.request.Request(userUrl,headers=header)
            userResponse = urllib.request.urlopen(userRequest).read()
            userResponse = userResponse.decode('utf-8') 
            userResponse = re.findall(r'({.*})',userResponse)#使用正则表达式提取Json
            #print(userResponse)
            userData = json.loads(userResponse[0])#字符串转化为json对象
            j = 0
            while j<len(userData['videolst'])-2:
                res.append([userId[i], userData['videolst'][j]['vid'],
                userData['videolst'][j]['title'], userData['videolst'][j]['uploadtime'],
                userData['videolst'][j]['desc'], toInt(userData['videolst'][j]['play_count'])])
                j+=1
            page+=1
        i+=1
    # print(res)
    return res
# v_qq(['7fbed6756baeba7fe370ba49c9e883e0'])
