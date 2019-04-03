import datetime
import time
import Video


def function():
    #weiboVideo()
    time.sleep(60)

def main(m=0):
    while True:
        while True:
            now = datetime.datetime.now()
            if now.minute == m:
                break
            time.sleep(30)
        function()
main()