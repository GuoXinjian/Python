import re
import socket
import signal
import multiprocessing
import time
 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 8602 # 端口8601、8602、12601、12602这几个端口号都是，但有时候有号些获取不到弹幕的信息，每个都试下总有一个可以
host = socket.gethostbyname('openbarrage.douyutv.com')
client.connect((host,port))
 
danmu = re.compile(b'txt@=(.+?)/')
user_id = re.compile(b'nn@=(.+?)/')


a = re.compile(b'@=')
b = re.compile(b'/')
c = re.compile(b'@A')
d = re.compile(b'@S')

 
def send_request_msg(msgstr):
    
    msg = msgstr.encode('utf-8')#协议规定所有协议内容均为 UTF-8 编码
 
 
    data_lenth = len(msg) + 8
    #data_lenth表示整个协议头的长度（消息长度），包括数据部分和头部，len(msg)就是数据部分，8就是头部的长度
 
    code = 689
    #根据协议消息类型字段用689
 
    msghead = int.to_bytes(data_lenth,4,'little') + int.to_bytes(data_lenth,4,'little') + int.to_bytes(code,4,'little')
    #msghead是按照斗鱼第三方协议构造的协议头
    #前2段表示的是消息长度，最后一个是消息类型
    #这里还有个值得注意的一点，发送给服务器的类型和服务器返回的类型都是bytes，因此要把数据信息通过int.to_bytes()变成bytes
    
    
    client.sendall(msghead)#发送协议头
 
    client.sendall(msg)#发送消息请求
 
 
def get_danmu(roomid):
 
    denglu_msg = 'type@=loginreq/roomid@={}/\0'.format(roomid)#登录请求消息,最后面的'\0',是协议规定在数据部分结尾必须是'\0'
 
    send_request_msg(denglu_msg)
 
    join_room_msg = 'type@=joingroup/rid@={}/gid@=-9999/\0'.format(roomid)#加入房间分组消息
 
    send_request_msg(join_room_msg)
 
    while True:
        
        data = client.recv(9999)
        #这个data就是服务器向客户端发送的消息
        #具体的信息可以看斗鱼弹幕第三方接入协议
        
        # print(re.sub(d,b'/',data).decode('utf-8'))
        danmu_username = re.findall(user_id,data)
        dammu_content = re.findall(danmu,data)
        #print(data)
 
        if not data:
            break
        else:
            for i in range(0,len(danmu_username)):
                try:
                    print('[{}]:{}'.format(danmu_username[i].decode('utf-8'),dammu_content[i].decode('utf-8')))
                                #返回的数据是bytes型，所以要用decode方法来解码
                except:
                    continue
 
 
def keeplive():
    #维持与后台的心跳
    #关于心跳消息，协议中有详细的解释
    n=0
    while True:
        live_msg = 'type@=keeplive/tick@=' + str(int(time.time())) + '/\0'
        # live_msg = 'type@=mrkl' + '/\0'
        send_request_msg(live_msg)
        print('keep alive   '+str(n))
        n+=1
        time.sleep(15)
 
 
def logout():
    out_msg = 'type@=logout/'
    send_request_msg(out_msg)
    print('已退出服务器！')
 
 
def signal_handler(signal,frame):
    #捕捉ctrl + c的信号，即signal.SIGINT
 
    p1.terminate()#结束进程
    p2.terminate()#结束进程
    logout()
 
 
if __name__ == '__main__':
    
    roomid = 100       #房间号,主播开播才能获取到信息
    
    signal.signal(signal.SIGINT,signal_handler)
 
    p1 = multiprocessing.Process(target = get_danmu,args = (roomid,))
    p2 = multiprocessing.Process(target = keeplive)
 
    p1.start()
    p2.start()