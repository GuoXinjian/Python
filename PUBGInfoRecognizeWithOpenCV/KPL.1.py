import pytesseract
import time
import cv2
from multiprocessing import Process,Queue,Pool
import numpy as np


imgqueue=Queue()
def recognize(lis):
    # print(lis)
    # time.sleep(1)
    return 1




def chopchr(img):
    h,w=img.shape
    v=[0]*w
    z=[0]*h
    a=0
    for x in range(w):
        for y in range(h):
            # print(img[y,x])
            if img[y,x]==0:
                a+=1
        v[x]=a
        a=0
    # print(v)

    lis=[]
    l=0
    r=1
    while r <len(v):
        if v[r]>0 and v[r-1]==0:
            l=r
        elif v[r]==0 and v[r-1]>0:
            lis.append([l,r])
            l=r
        elif v[r]==0 and v[r-1]==0:
            l=r
        r+=1
    print('b-1',time.time())  
    value=recognize(lis)
    return value
    


def chopnum(imgqueue):
    while True:
        img=imgqueue.get(True)
        
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,pic = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)


        bluedragon=pic[235:270,587:612]
        bluetower=pic[235:270,672:695]
        bluepoint=pic[233:272,855:927]
        reddragon=pic[235:270,1350:1375]
        redtower=pic[235:270,1258:1281]
        redpoint=pic[233:272,990:1060]
        img10=pic[230:270,760:860]
        img11=pic[335:370,800:900]
        img12=pic[460:495,800:900]
        img13=pic[585:620,800:900]
        img14=pic[710:745,800:900]
        img15=pic[835:870,800:900]
        img20=pic[230:270,1100:1200]
        img21=pic[335:370,1685:1785]
        img22=pic[460:495,1685:1785]
        img23=pic[585:620,1685:1785]
        img24=pic[710:745,1685:1785]
        img25=pic[835:870,1685:1785]

        cv2.moveWindow('bd',200,0)
        cv2.imshow('bd',bluedragon)
        cv2.moveWindow('bt',400,0)
        cv2.imshow('bt',bluetower)
        cv2.moveWindow('bp',600,0)
        cv2.imshow('bp',bluepoint)
        cv2.moveWindow('rd',200,200)
        cv2.imshow('rd',reddragon)
        cv2.moveWindow('rt',400,200)
        cv2.imshow('rt',redtower)
        cv2.moveWindow('rp',600,200)
        cv2.imshow('rp',redpoint)
        cv2.imshow('10',img10)
        cv2.waitKey(1)
        cv2.moveWindow('10',0,400)
        cv2.imshow('11',img11)
        cv2.waitKey(1)
        cv2.moveWindow('11',200,400)
        cv2.imshow('12',img12)
        cv2.waitKey(1)
        cv2.moveWindow('12',400,400)
        cv2.imshow('13',img13)
        cv2.waitKey(1)
        cv2.moveWindow('13',600,400)
        cv2.imshow('14',img14)
        cv2.waitKey(1)
        cv2.moveWindow('14',800,400)
        cv2.imshow('15',img15)
        cv2.waitKey(1)
        cv2.moveWindow('15',1000,400)
        cv2.imshow('20',img20)
        cv2.waitKey(1)
        cv2.moveWindow('20',0,600)
        cv2.imshow('21',img21)
        cv2.waitKey(1)
        cv2.moveWindow('21',200,600)
        cv2.imshow('22',img22)
        cv2.waitKey(1)
        cv2.moveWindow('22',400,600)
        cv2.imshow('23',img23)
        cv2.waitKey(1)
        cv2.moveWindow('23',600,600)
        cv2.imshow('24',img24)
        cv2.waitKey(1)
        cv2.moveWindow('24',800,600)
        cv2.imshow('25',img25)
        cv2.waitKey(1)
        cv2.moveWindow('25',1000,600)
        imgdic={
            'bluedragon' : bluedragon,
            'bluetower'  : bluetower,
            'bluepoint'  : bluepoint,
            'reddragon'  : reddragon,
            'redtower'   : redtower,
            'redpoint'   : redpoint,
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
        resdic={}
        p=Pool(6)
        print('b',time.time())
        for key,img in imgdic.items():
            resdic[key]=p.apply_async(chopchr,args=(img,))
            # lis = chopchr(img)
            # value=recognize(lis)
        p.close()
        p.join()
        print('c',time.time())
        print(resdic)

def play(cap,imgqueue):
    frame=0
    while True:
        frame+=1
        ret,video = cap.read()
        cv2.imshow('video',video)
        cv2.waitKey(1)
        if frame%20==0 :#and frame>1*25*60:
            print('a',time.time())
            imgqueue.put(video)
            # chopnum(video)



    


if __name__=='__main__':
    cap = cv2.VideoCapture(3)
    pm = Process(target=chopnum,args=(imgqueue,))
    pw = Process(target=play,args=(cap,imgqueue,))
    pw.start()
    pm.start()
    pw.join()
    pm.terminate()

