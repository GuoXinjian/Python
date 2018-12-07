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
imgpath = r'C:\Users\2018091001\Desktop\456.png'
img = cv2.imread(imgpath)
#print(img[1])
'''
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)


gradX = cv2.Sobel(gray,ddepth=cv2.CV_32F,dx=1,dy=0,ksize=1)
gradY = cv2.Sobel(gray,ddepth=cv2.CV_32F,dx=0,dy=1,ksize=1)
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
'''

img=cv2.resize(img,(400,200))
cv2.imshow('img',img)
cv2.waitKey(1000)
sec=0
text = pytesseract.image_to_string(img,lang='eng')
print(text)











