import numpy as np 
import cv2
import sys
 
def CatVideo():
    cv2.namedWindow("CaptureFace")
    #1调用摄像头,也可以读取工作目录下的视频'/*/*/*.avi'
    cap=cv2.VideoCapture(0)
    #2人脸识别器分类器  GIT上面有开源的分类集，可以从下面的云盘里下载
    classfier=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
    color=(0,255,0)
    while cap.isOpened():
        ok,frame=cap.read()
        if not ok:
            break
        #3灰度转换
        grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #4人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        if len(faceRects) > 0:            #大于0则检测到人脸                                   
            for faceRect in faceRects:  #单独框出每一张人脸
                 x, y, w, h = faceRect  #5画图   
                 cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 3)
        cv2.imshow("CaptureFace",frame)
        if cv2.waitKey(10)&0xFF==ord('q'):
            break
 
    cap.release()
    cv2.destroyAllWindows()
 
CatVideo()