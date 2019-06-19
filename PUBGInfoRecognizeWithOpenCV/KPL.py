import time
import cv2
# from multiprocessing import Pool
import numpy as np
import sqlalchemy
from KPLServer import KPL,db
# TODO 对数字图片尺寸进行标准化处理


#######   training part    ############### 
samples = np.loadtxt(r'D:\Python\PUBGInfoRecognizeWithOpenCV\generalsamples.data',np.float32)
responses = np.loadtxt(r'D:\Python\PUBGInfoRecognizeWithOpenCV\generalresponses.data',np.float32)
responses = responses.reshape((responses.size,1))

model = cv2.ml.KNearest_create()
model.train(samples,cv2.ml.ROW_SAMPLE,responses)


init = KPL()
init.bluedragon=0
init.bluetower =0
init.bluepoint =0
init.blueall   =1500
init.reddragon =0
init.reddragon =0
init.redtower  =0
init.redpoint  =0
init.redall    =1500

init.b1        =300
init.b2        =300
init.b3        =300
init.b4        =300
init.b5        =300
init.r1        =300
init.r2        =300
init.r3        =300
init.r4        =300
init.r5        =300

db.session.add(init)
db.session.commit()

def first(cnt):
    [x,y,w,h] = cv2.boundingRect(cnt)
    return x

def recognize(img,height=22):
    ret,thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU) #二值化
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #找到图片中的数字
    contours.sort(key=first) #数字从左到右排序
    resnum=''
    for cnt in contours:
        
        area=cv2.contourArea(cnt)
        if area>20 and area<800: #取面积适中的数字
            [x,y,w,h] = cv2.boundingRect(cnt)
            # print([x,y,w,h])
            if  h>height:
                cv2.rectangle(thresh,(x,y),(x+w,y+h),(0,255,255),1) #在图上画框
                roi = thresh[y:y+h,x:x+w]
                roismall = cv2.resize(roi,(10,10))
                roismall = roismall.reshape((1,100))
                roismall = np.float32(roismall)
                retval, results, neigh_resp, dists = model.findNearest(roismall, k = 1)
                string = str(int((results[0][0])))
                resnum+=string
                # print(string)
    # print(resnum)
    try:
        resnum=int(resnum)
        return resnum
    except:
        pass

    
def chopnum(img):
    global init
    pic = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #确定数字的标准位置
    bluedragon=pic[230:275,585:615]
    bluetower=pic[230:275,670:695]
    bluepoint=pic[230:275,855:930]
    reddragon=pic[230:275,1350:1380]
    redtower=pic[230:275,1255:1285]
    redpoint=pic[230:275,980:1060]
    # img10=pic[230:268,760:860]
    img11=pic[330:375,795:908]
    img12=pic[445:500,795:908]
    img13=pic[580:625,795:908]
    img14=pic[705:750,795:908]
    img15=pic[830:875,795:908]
    # img20=pic[230:268,1100:1200]
    img21=pic[330:375,1680:1790]
    img22=pic[445:500,1680:1790]
    img23=pic[580:625,1680:1790]
    img24=pic[705:750,1680:1790]
    img25=pic[830:875,1680:1790]

    pointdic={   #较大的数字
        'bluepoint'  : bluepoint,
        'redpoint'   : redpoint,
    }
    
    imgdic={     #较小的数字
        'bluedragon' : bluedragon,
        'bluetower'  : bluetower,
        'reddragon'  : reddragon,
        'redtower'   : redtower,
        'img11'      : img11,
        'img12'      : img12,
        'img13'      : img13,
        'img14'      : img14,
        'img15'      : img15,
        'img21'      : img21,
        'img22'      : img22,
        'img23'      : img23,
        'img24'      : img24,
        'img25'      : img25,
    }
    
    
    #单线程方案
    resdic={}
    for key,img in imgdic.items():
        resdic[key]=recognize(img,22)
    for key,img in pointdic.items():
        resdic[key]=recognize(img,29)
    
    #多线程方案
    
    '''
    p=Pool(6)
    # print('b',time.time())
    for key,img in imgdic.items():
        # print('c-1',time.time())
        resdic[key]=p.apply_async(chopchr,args=(key,img,))
        # print('c-2',time.time())
        # lis = chopchr(img)
        # value=recognize(lis)
    p.close()
    p.join()
    '''
    # print(resdic['img11'])
    # try:
    res=KPL()
    res.bluedragon = resdic['bluedragon']
    res.bluetower  = resdic['bluetower']
    res.bluepoint  = resdic['bluepoint']
    res.reddragon  = resdic['reddragon']
    res.redtower   = resdic['redtower']
    res.redpoint   = resdic['redpoint']
    res.b1         = resdic['img11']
    res.b2         = resdic['img12']
    res.b3         = resdic['img13']
    res.b4         = resdic['img14']
    res.b5         = resdic['img15']
    res.r1         = resdic['img21']
    res.r2         = resdic['img22']
    res.r3         = resdic['img23']
    res.r4         = resdic['img24']
    res.r5         = resdic['img25']
    res.blueall    = resdic['img11']+resdic['img12']+resdic['img13']+resdic['img14']+resdic['img15']
    res.redall     = resdic['img21']+resdic['img22']+resdic['img23']+resdic['img24']+resdic['img25']
    print('a',resdic)
    #容错

    delta={
        'bluedragon' :init.bluedragon-res.bluedragon,
        'bluetower'  :init.bluetower-res.bluetower,
        'bluepoint'  :init.bluepoint-res.bluepoint,
        'blueall'    :init.blueall-res.blueall,

        'reddragon'  :init.reddragon-res.reddragon,
        'redtower'   :init.redtower-res.redtower,
        'redpoint'   :init.redpoint-res.redpoint,
        'redall'     :init.redall-res.redall,
    }
    if delta['bluedragon']>0 or delta['bluedragon']<-2:
        res.bluedragon=init.bluedragon
        print('BD')
    if delta['bluetower']>0 or delta['bluetower']<-2:
        res.bluetower=init.bluetower
        print('BT')
    if delta['bluepoint']>0 or delta['bluepoint']<-4:
        res.bluepoint=init.bluepoint
        print('BP')
    if delta['reddragon']>0 or delta['reddragon']<-2:
        res.reddragon=init.reddragon
        print('RD')
    if delta['redtower']>0 or delta['redtower']<-2:
        res.redtower=init.redtower
        print('RT')
    if delta['redpoint']>0 or delta['redpoint']<-4:
        res.redpoint=init.redpoint
        print('RP')

    db.session.add(res)
    db.session.commit()
    print('b',resdic)
    init=res
    # except:
    #     pass




def play(cap):
    frame=0
    # ret,video = cap.read()
    # cv2.imshow('video',video)
    # cv2.waitKey(1)
    # chopnum(video)

    while True:
        frame+=1
        ret,video = cap.read()
        cv2.imshow('video',video)
        cv2.waitKey(1)
        #鉴于计算耗时，跨帧识别，不每一帧识别
        if frame%10==0:# and frame>23*25*60:
            chopnum(video)
            
            



    


if __name__=='__main__':

    capindex=1 #视频输入源的序号
    # capindex=r'C:/Users/follo/Desktop/1.jpg'
    # capindex=r'C:/Users/follo/Desktop/装备栏图像.mp4'
    cap = cv2.VideoCapture(capindex)
    cap.set(3,1920)
    cap.set(4,1080)

    play(cap)
