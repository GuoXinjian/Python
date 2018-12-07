import cv2
import numpy as np
import time
#import matplotlib
#  228:342,5:119 362:476,5:119 493:607,5:119 626:740,5:119 758:872,5:119     
imgpath = 'C:\\Users\\2018091001\\Desktop\\heros2\\'
videopath = 'C:\\Users\\2018091001\\Desktop\\2017-04-02-21-42-30-VOD.ts'
vod = cv2.VideoCapture(videopath)



i=1
models = []
while i<600:
    img = imgpath+str(i)+'.png'
    model = cv2.imread(img)
    # cv2.imshow('1',model)
    # cv2.waitKey(3000)
    #print(img)
    if type(model).__name__ == 'ndarray':
        model = cv2.resize(model,(114,114))
        X1 = cv2.calcHist([model],[0],None,[256],[0,256])
        X1=cv2.normalize(X1,X1,0,1,cv2.NORM_MINMAX,-1)
        X2 = cv2.calcHist([model],[1],None,[256],[0,256])
        X2=cv2.normalize(X2,X2,0,1,cv2.NORM_MINMAX,-1)
        X3 = cv2.calcHist([model],[2],None,[256],[0,256])
        X3=cv2.normalize(X3,X3,0,1,cv2.NORM_MINMAX,-1)
        models.append([X1,X2,X3])
    i+=1
    
print(len(models))

while True:
    ret,video = vod.read()
    hero=[video[228:342,5:119],video[362:476,5:119],video[493:607,5:119],video[626:740,5:119],video[758:872,5:119]]
    cv2.imshow('1',hero[1])
    cv2.waitKey(3000)
    j=0
    
    heros = [] 
    while j<5:
        H1 =cv2.calcHist([hero[j]],[0],None,[256],[0,256])
        H1=cv2.normalize(H1,H1,0,1,cv2.NORM_MINMAX,-1)
        H2 =cv2.calcHist([hero[j]],[1],None,[256],[0,256])
        H2=cv2.normalize(H2,H2,0,1,cv2.NORM_MINMAX,-1)
        H3 =cv2.calcHist([hero[j]],[2],None,[256],[0,256])
        H3=cv2.normalize(H3,H3,0,1,cv2.NORM_MINMAX,-1)
        x=0
        # print(type(H2))
        # print(H2)
        similarity=0
        res=0
        idx=0
               
        while x<len(models):
            #print(type(models[x][0]))
            similarity = cv2.compareHist(H1,models[x][0],0)+ cv2.compareHist(H2,models[x][1],0)+cv2.compareHist(H3,models[x][2],0)
            if similarity>=res:
                res=similarity
                idx=x
            x+=1
        heros.append([j,idx,res])
        j+=1
    print(heros)
    time.sleep(1)





