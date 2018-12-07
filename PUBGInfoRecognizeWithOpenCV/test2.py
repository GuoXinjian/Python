# -*- coding:utf-8  -*-


# 获取战队LOGO 
# 结合文字训练识别库

# 载入右上角击杀信息
# 转灰度
# 二值化
# 识别轮廓
# 识别内容
# 记录内容
# 将识别出的内容与已发生的内容比对，若存在该信息，则忽略该信息。
# 输出新信息
# 记录、统计击杀、存活情况

import time
import cv2
import pytesseract
imgpath = r'C:\Users\2018091001\Desktop\123.png'
img = cv2.imread(imgpath)
'''
cv2.imshow('img',img[:,:,0])
cv2.waitKey(10000)
cv2.imshow('img',img[:,:,1])
cv2.waitKey(10000)
cv2.imshow('img',img[:,:,2])#红色通道
cv2.waitKey(10000)
'''
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('img',gray)
#cv2.waitKey(10000)
ret,thresh1 = cv2.threshold(gray,170,255,cv2.THRESH_BINARY)
#cv2.imshow('img',thresh1)
#cv2.waitKey(10000)
#gray = cv2.erode(thresh1,None,iterations=3)#颜色腐蚀
'''
gradX = cv2.Sobel(gray,ddepth=cv2.CV_32F,dx=1,dy=0,ksize=1)
gradY = cv2.Sobel(gray,ddepth=cv2.CV_32F,dx=0,dy=1,ksize=1)
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
'''

h,w=thresh1.shape
v=[0]*w
z=[0]*h
a=0
for x in range(w):
    for y in range(h):
        if thresh1[y,x]==0:
            a+=1
    v[x]=a
    a=0
print(v)
r=[]
l=[]
for i in range(4,w-4):
    if v[i-2]!=h and v[i+1]==v[i+2]==v[i+3]==v[i-1]==v[i]==h:
        r.append(i)
    if v[i+2]!=h and v[i-1]==v[i-2]==v[i-3]==v[i+1]==v[i]==h and len(r)!=0:
        l.append(i)


if len(r)-len(l)==1:
    l.insert(0,0)
print(l,r)
#knn = cv2.createBackgroundSubtractorKNN(detectShadows = True)
def drawCnt(fn, cnt):
  if cv2.contourArea(cnt) > 1600:
    (x, y, w, h) = cv2.boundingRect(cnt)
    cv2.rectangle(fn, (x, y), (x + w, y + h), (255, 255, 0), 2)

#thresh =knn.apply(thresh1)

#cv2.imshow('img',thresh)
#cv2.waitKey(10000)
v1=thresh1[:,l[0]:r[0]]
v2=thresh1[:,l[1]:r[1]]
#print(l[1],r[1])
v3=thresh1[:,l[2]:r[2]]
v4=thresh1[:,l[3]:r[3]]
v5=thresh1[:,l[4]:r[4]]

cv2.imwrite(r'C:\Users\2018091001\Desktop\v1.png',v1)
cv2.imwrite(r'C:\Users\2018091001\Desktop\v2.png',v2)
cv2.imwrite(r'C:\Users\2018091001\Desktop\v3.png',v3)
cv2.imwrite(r'C:\Users\2018091001\Desktop\v4.png',v4)
cv2.imwrite(r'C:\Users\2018091001\Desktop\v5.png',v5)
v3=cv2.resize(v3,(400,120))
cv2.imwrite(r'C:\Users\2018091001\Desktop\v2.png',v2)
cv2.imshow('img',v3)
cv2.waitKey(1000)
text = pytesseract.image_to_string(v3,lang='eng')
print(text)











