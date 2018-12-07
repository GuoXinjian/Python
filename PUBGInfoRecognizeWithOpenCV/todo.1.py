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
videopath = r'rtsp://0.0.0.1/stream1'
vod = cv2.VideoCapture(videopath)
sec=0
while True:
    sec+=1
    ret,video = vod.read()
    

    cv2.imshow('1111',video)
    cv2.waitKey(1)
    #text = pytesseract.image_to_string(timeNow)
    #print(sec,text)
    #time.sleep(0.05)










