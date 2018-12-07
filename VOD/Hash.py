# -*- coding:utf-8  -*-
import cv2
import numpy as np
import time
#  228:342,5:119 362:476,5:119 493:607,5:119 626:740,5:119 758:872,5:119     
imgpath = 'C:\\Users\\2018091001\\Desktop\\heros2\\'
videopath = 'C:\\Users\\2018091001\\Desktop\\2017-04-02-21-42-30-VOD.ts'
vod = cv2.VideoCapture(videopath)
dic=('韩信','项羽','杨戬','花木兰','嬴政')
def p_hash(src):
    # Step1. 把图像缩小为16 * 16,并转化为灰度图
    src = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    src = cv2.resize(src, (16, 16), cv2.INTER_LINEAR)
    # Step2. 计算256个像素的灰度均值
    avg = sum([sum(src[i]) for i in range(16)]) / 256
    # Step3. 与平均值比较，生成01字符串
    string = ''
    print(src)
    for i in range(16):
        '''
        for j in range(8):
            if src[i][j]<=avg:
                src[i][j]=0
            else:
                src[i][j]=1
        '''
        string += ''.join(map(lambda i: '0' if i < avg else '1', src[i]))
    # Step4. 计算hash值
    result = ''
    for i in range(0, 256, 4):
        result += ''.join('%x' % int(string[i: i + 4], 2))
    print(result)
    return result


def hamming(str1, str2):
    if len(str1) != len(str2):
        return
    count = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

#获取模板图片集
i=1
models = []
while i<600:
    img = imgpath+str(i)+'.png'
    model = cv2.imread(img)
    if type(model).__name__ == 'ndarray':
        models.append(p_hash(model))
    i+=1   

sec = 0
while True:
    sec+=1
    ret,video = vod.read()
    hero=[video[228:342,5:119],video[362:476,5:119],video[493:607,5:119],video[626:740,5:119],video[758:872,5:119]]
    j=0
    heros = [] 
    while j<5:
        h = p_hash(hero[j])
        x=0
        similarity=0
        res=200
        idx=0         
        while x<len(models):
            similarity = hamming(h,models[x])
            if similarity<=res:
                res=similarity
                idx=x
            x+=1
        heros.append([sec,j,dic[idx],res])
        j+=1
    print(heros)
    #time.sleep(0.01)