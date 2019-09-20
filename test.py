import requests

url = 'http://www.fangline.cn/gather.do?method=listResources'



headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; vivo X9Plus Build/LMY48Z) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Safari/537.36 MicroMessenger/6.6.7.1321(0x26060736) NetType/WIFI Language/zh_CN',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'SESSION=51c45b10-6ecb-403d-82a1-297cd4142028; ant.mobile.wx46cbc2feb419e889=onWKSweQELTTRDKEdUqsccGkFqF4; SERVERID=b1c2ca27bdcbfbfd61e99ab704c80e0f|1567736969|1567736760'

}

i=1
while i<5:
    data = {
        'pageNo':'1',
        'pageSize':'25',
        'bizType':'sell',
        'searchType':'1',
        'status':'3,2,4',
        'orderCol':'createTime',
    }
    res=requests.post(url, data=data,headers=headers)
    print(res.content)
    i+=1