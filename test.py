import cv2

for i in range(10):
    cap=cv2.VideoCapture(i)
    ret,video=cap.read()
    try:
        cv2.imshow(str(i),video)
        cv2.waitKey(1000)
    except:
        print(i)



cap=cv2.VideoCapture(3)
cap.set(3,1920)
cap.set(4,1080)
print(cap.get(3),cap.get(4))
while True:

    ret,video = cap.read()
    cv2.imshow('video',video)
    cv2.waitKey(1)



# app=Flask(__name__)

# @app.route('/')
# def index():
#     return '<p>Hello</p>'
# @app.route('/login')
# def login():
#     return 'login'
# app.run('0.0.0.0')