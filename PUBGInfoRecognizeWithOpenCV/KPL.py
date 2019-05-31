import pytesseract
import time
import cv2
from multiprocessing import Pool
import numpy as np
import random
import matplotlib.pyplot as plt

def recognize(v):
    num = 0

   
    startIndex = 0
    endIndex = len(v)-1

    # 判断0, 前3增 后3降，12~18相等小于等于6（总和35）
    if( (v[startIndex] < v[startIndex+1]) and (v[startIndex+1] <= v[startIndex+2]) and (v[endIndex] < v[endIndex-1]) and (v[endIndex-1] <= v[endIndex-2]) and (sum(v[startIndex+11:startIndex+16]) <= 35) ):
        return 0

    # 判断1, 倒数5位总和小于等于20
    if (sum(v[endIndex-4:endIndex+1]) <= 20):
        return 1

    # 判断2, 倒数2位求和大于25，并且是倒数第5位的2倍以上
    a=sum(v[endIndex - 1:])
    b=v[endIndex] - v[endIndex-4] * 2
    if ( (sum(v[endIndex - 1:]) > 25) and (v[endIndex] > v[endIndex-4] * 2) ):
        return 2

    # 判断3, 前3增后3降，7~9,15~16小于5（求和10）
    if ( (v[startIndex] < v[startIndex + 1]) and (v[startIndex + 1] <= v[startIndex + 2])
            and (v[endIndex] < v[endIndex - 1]) and (v[endIndex - 1] <= v[endIndex - 2])
            and (sum(v[startIndex + 7:startIndex + 8]) < 10)
            and (sum(v[startIndex + 15:startIndex + 17]) < 10) ):
        return 3

    # 判断4, 倒数3小于5，倒数6~7相等大于15
    if ( (max(v[endIndex-2:]) < 5) and (min(v[endIndex-7:endIndex-5]) > 12) ):
        return 4

    # 判断5, 前3相等大于10小于14
    if ( (max(v[startIndex:startIndex+3]) < 14) and (min(v[startIndex:startIndex+3]) > 10) ):
        return 5

    # 判断6, 前3增后3降，7~9小于5,15~16大于5（求和10）
    if ((v[startIndex] < v[startIndex + 1]) and (v[startIndex + 1] <= v[startIndex + 2])
            and (v[endIndex] < v[endIndex - 1]) and (v[endIndex - 1] <= v[endIndex - 2])
            and (sum(v[startIndex + 7:startIndex + 9]) < 10)
            and (sum(v[startIndex + 15:startIndex + 17]) > 10)):
        return 6


    # 判断7, 前3相等大于14
    if ((max(v[startIndex:startIndex + 3]) < 18) and (min(v[startIndex:startIndex + 3]) > 14)):
        return 7


    # 判断8, 前3增后3降，7~9,15~16大于5（求和10）
    if ((v[startIndex] < v[startIndex + 1]) and (v[startIndex + 1] <= v[startIndex + 2])
            and (v[endIndex] < v[endIndex - 1]) and (v[endIndex - 1] <= v[endIndex - 2])
            and (sum(v[startIndex + 7:startIndex + 9]) > 10)
            and (sum(v[startIndex + 15:startIndex + 17]) > 10)):
        return 8


    # 判断9, 前3增后3降，7~9大于5,15~16小于5（求和10）
    if ((v[startIndex] < v[startIndex + 1]) and (v[startIndex + 1] <= v[startIndex + 2])
            and (v[endIndex] < v[endIndex - 1]) and (v[endIndex - 1] <= v[endIndex - 2])
            and (sum(v[startIndex + 7:startIndex + 9]) > 10)
            and (sum(v[startIndex + 15:startIndex + 17]) < 10)):
        return 9



def chopchr(img):
    # print('b-1',time.time())  
    ret,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # cv2.imwrite('D:%s'%random.random(),img)
    cv2.imshow('img',img)
    cv2.waitKey(1000)
    h,w=img.shape
    # print(h,w)
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
    print(v)


    h,w=img.shape
    
    lis=[]
    l=0
    r=1
    while r <len(v):
        if v[r]>0 and v[r-1]==0:
            l=r
        elif v[r]==0 and v[r-1]>0:
            lis.append([l+2,r-1])
            l=r
        elif v[r]==0 and v[r-1]==0:
            l=r
        r+=1
    print(lis)

    for l in lis:
        oneimg=img[:,l[0]:l[1]]
        h,w=oneimg.shape
        # print(onechr[1]-onechr[0],h,w)
        o=[0]*w
        z=[0]*h
        a=0
        for x in range(h):
            for y in range(w):
                # print(img[y,x])
                if oneimg[x,y]==0:
                    a+=1
                    
            z[x]=a
            a=0

        # onevalue=v[l[0]:l[1]]
        
        
        while True:
            if z[0]==0:
                z.pop(0)
            else:
                break
        while True:
            if z[-1]==0:
                z.pop()
            else:
                break
        print(z)
        value = recognize(z)
        print(value)
    return value
    
    # print('b-2',time.time())  
    # print(lis)
    # plt.bar(list(range(w)),v,label='1')
    # plt.legend()
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.show()

    # resnum=''

    # for onechr in lis:
    #     if onechr[1]-onechr[0]<=10:
    #         resnum+='1'
    #     else:



            # onelis=v[onechr[0]:onechr[1]]
            # # print(onelis)
            # if max(onelis)<18:
            #     if onelis[-1]<5:
            #         resnum+='7'
            #     else:
            #         resnum+='2'
            # elif max(onelis[-6:])>20:
            #     if min(onelis[-3:-1])<5:
            #         resnum+='4'
            #     elif max(onelis[3:6])>20:
            #         onenum=img[:,onechr[0]:onechr[1]+1]
            #         h,w=onenum.shape
            #         print(h,w)
            #         o=[0]*w
            #         z=[0]*h
            #         a=0
            #         for x in range(h):
            #             for y in range(w):
            #                 # print(img[y,x])
            #                 if onenum[x,y]==0:
            #                     a+=1
            #             z[x]=a
            #             a=0
            #         # plt.bar(list(range(h)),z,label='1')
            #         # plt.legend()
            #         # plt.xlabel('x')
            #         # plt.ylabel('y')
            #         # plt.show()
    
            #         if max(onelis[12:17])>10:
            #             print('8',z)
            #             plt.bar(list(range(h)),z,label='8')
            #             plt.legend()
            #             plt.xlabel('x')
            #             plt.ylabel('y')
            #             plt.show()
            #             resnum+='8'
            #         else:
            #             print('0',z)
            #             plt.bar(list(range(h)),z,label='0')
            #             plt.legend()
            #             plt.xlabel('x')
            #             plt.ylabel('y')
            #             plt.show()
            #             resnum+='0'


                    
            #     elif max(onelis[3:6])>15:
            #         resnum+='9'
            #     else:
            #         resnum+='3'


            # else:
                # onenum=img[:,onechr[0]:onechr[1]]
                
                # h,w=onenum.shape
                # print(onechr[1]-onechr[0],h,w)
                # o=[0]*w
                # z=[0]*h
                # a=0
                # for x in range(h):
                #     for y in range(w):
                #         # print(img[y,x])
                #         if onenum[x,y]==0:
                #             a+=1
                #     z[x]=a
                #     a=0
                # cv2.imshow('onechr',onenum)
                # cv2.waitKey(1000)
                # plt.bar(list(range(h)),z,label='x')
                # plt.legend()
                # plt.xlabel('x')
                # plt.ylabel('y')
                # plt.show()
                # print(z)
                # cv2.imshow('onechr',onenum)
                # cv2.waitKey(1000)

                # if z[0]>10 and abs(z[0]-z[1])<2 and min(z[4:7])<5:
                #     resnum+='5'
                #     print('5',z)
                #     plt.bar(list(range(h)),z,label='5')
                #     plt.legend()
                #     plt.xlabel('x')
                #     plt.ylabel('y')
                #     plt.show()
                # else:
                #     resnum+='6'
                #     print('6',z)
                #     plt.bar(list(range(h)),z,label='6')
                #     plt.legend()
                #     plt.xlabel('x')
                #     plt.ylabel('y')
                #     plt.show()
                
    
    # value=recognize(lis)
    # print(resnum)
    # cv2.imwrite('%s.jpg'%resnum,img)
    # return value
    


def chopnum(img):

    # print('a',time.time())
    # gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # ret,pic = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

    pic = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    bluedragon=pic[238:268,589:610]
    bluetower=pic[238:268,672:695]
    bluepoint=pic[233:273,855:927]
    reddragon=pic[238:268,1352:1368]
    redtower=pic[238:268,1258:1281]
    redpoint=pic[233:273,990:1060]
    img10=pic[230:268,760:860]
    img11=pic[338:368,800:900]
    img12=pic[462:492,800:900]
    img13=pic[588:618,800:900]
    img14=pic[712:742,800:900]
    img15=pic[836:866,800:900]
    img20=pic[230:268,1100:1200]
    img21=pic[338:368,1685:1785]
    img22=pic[462:492,1685:1785]
    img23=pic[588:618,1685:1785]
    img24=pic[712:742,1685:1785]
    img25=pic[836:866,1685:1785]

    # cv2.moveWindow('bd',200,0)
    # cv2.imshow('bd',bluedragon)
    # cv2.moveWindow('bt',400,0)
    # cv2.imshow('bt',bluetower)
    # cv2.moveWindow('bp',600,0)
    # cv2.imshow('bp',bluepoint)
    # cv2.moveWindow('rd',200,200)
    # cv2.imshow('rd',reddragon)
    # cv2.moveWindow('rt',400,200)
    # cv2.imshow('rt',redtower)
    # cv2.moveWindow('rp',600,200)
    # cv2.imshow('rp',redpoint)
    # cv2.imshow('10',img10)
    # cv2.waitKey(1)
    # cv2.moveWindow('10',0,400)
    # cv2.imshow('11',img11)
    # cv2.waitKey(1)
    # cv2.moveWindow('11',200,400)
    # cv2.imshow('12',img12)
    # cv2.waitKey(1)
    # cv2.moveWindow('12',400,400)
    # cv2.imshow('13',img13)
    # cv2.waitKey(1)
    # cv2.moveWindow('13',600,400)
    # cv2.imshow('14',img14)
    # cv2.waitKey(1)
    # cv2.moveWindow('14',800,400)
    # cv2.imshow('15',img15)
    # cv2.waitKey(1)
    # cv2.moveWindow('15',1000,400)
    # cv2.imshow('20',img20)
    # cv2.waitKey(1)
    # cv2.moveWindow('20',0,600)
    # cv2.imshow('21',img21)
    # cv2.waitKey(1)
    # cv2.moveWindow('21',200,600)
    # cv2.imshow('22',img22)
    # cv2.waitKey(1)
    # cv2.moveWindow('22',400,600)
    # cv2.imshow('23',img23)
    # cv2.waitKey(1)
    # cv2.moveWindow('23',600,600)
    # cv2.imshow('24',img24)
    # cv2.waitKey(1)
    # cv2.moveWindow('24',800,600)
    # cv2.imshow('25',img25)
    # cv2.waitKey(1)
    # cv2.moveWindow('25',1000,600)
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
    chopchr(img11)
    '''
    p=Pool(6)
    # print('b',time.time())
    for key,img in imgdic.items():
        # print('c-1',time.time())
        resdic[key]=p.apply_async(chopchr,args=(img,))
        # print('c-2',time.time())
        # lis = chopchr(img)
        # value=recognize(lis)
    p.close()
    p.join()

    '''
    # print('c',time.time())
    # print(resdic)

def play(cap):
    frame=0
    while True:
        frame+=1
        ret,video = cap.read()
        cv2.imshow('video',video)
        cv2.waitKey(1)
        if frame%20==0 :#and frame>1*25*60:

            chopnum(video)



    


if __name__=='__main__':
    cap = cv2.VideoCapture(3)

    play(cap)
    # v=[9, 11, 13, 8, 6, 5, 4, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 3, 3, 13, 13, 13]
    # r=recognize(v)
    # print(r)