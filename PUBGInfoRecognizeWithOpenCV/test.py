import cv2

for i in range(10):
    cap=cv2.VideoCapture(i+cv2.CAP_ANY)
    cap.set(3,1920)
    cap.set(4,1080)
    ret,video=cap.read()
    try:
        cv2.imshow('%s'%i,video)
        cv2.waitKey(0)
    except:
        print(i)