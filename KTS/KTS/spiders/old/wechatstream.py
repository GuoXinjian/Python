import requests,datetime,time
import myemail


'''
loginurl = 'https://game.weixin.qq.com/cgi-bin/gameweappauthwap/login'

data = {"code":"071Q2Nn51wvLbT1cymm51j2Kn51Q2Nn5","need_openid":'true'}

response = requests.get(loginurl,params=data)

print(response.content)
'''

#连接后 生成session_id 重新连接或一段时间后session_id改变导致url改变

url = 'https://gamelivechatroom.weixin.qq.com/cgi-bin/livechatroom-bin/esportrecvmsg?auth_type=1&data_info={"base_request":{"roomid":100268,},"limitcnt":40}&session_id=h7Uqevm7QwLN8OHWVQ-yqA@oPof80L3JV9xx_rET3I-tbzF90IE'

while True:
    try:
        res = requests.get(url,verify=False)
        print(res.json())
        time.sleep(5)
    except Exception as e:
        content = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+':'+str(e)
        print(content)
        time.sleep(5)
        #myemail.mail('微信直播',content)
        break
