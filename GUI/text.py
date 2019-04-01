import msvcrt,time


n=0
while True:
    n+=1
    print(n)
    time.sleep(2)
    if ord(msvcrt.getch())>50:
        break


# print(time.strftime('%Y%m%d',time.localtime(time.time())))