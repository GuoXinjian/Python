from tkinter import *
from tkinter import ttk,filedialog,messagebox
import time,datetime
import openpyxl
from Models import *
import sqlalchemy
import pymysql
from pyecharts import Line
import pyecharts,pyecharts_snapshot,jupyter_echarts_pypkg,jinja2


root = Tk()
root.title('直播间数据查询下载')
root.geometry('300x200')
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
starttime=today
endtime = '2019-03-23'
def GetTimeline(start,end,time_level):
    time_level=time_level

    if not start:
        starttime=datetime.datetime.now().strftime('%Y-%m-%d')
        starttime=datetime.datetime.strptime(starttime,'%Y-%m-%d')
        starttime=starttime+datetime.timedelta(days=-1,hours=5)
    elif len(start)==10:
        starttime=datetime.datetime.strptime(start,'%Y-%m-%d')
    elif len(start)==19:
        starttime=datetime.datetime.strptime(start,'%Y-%m-%d %H:%M:%S')
    if not end:
        endtime = starttime + datetime.timedelta(days=1)
    elif len(start)==10:
        endtime=datetime.datetime.strptime(end,'%Y-%m-%d')
    elif len(start)==19:
        endtime=datetime.datetime.strptime(end,'%Y-%m-%d %H:%M:%S')
    endtime+=datetime.timedelta(minutes= (time_level if endtime.minute//time_level else 0))
    str_starttime=starttime.strftime('%Y-%m-%d %H:%M:%S')
    str_endtime=endtime.strftime('%Y-%m-%d %H:%M:%S')

    print(str_starttime)
    print(str_endtime)

    timeline=[]
    t=starttime + datetime.timedelta(minutes=15 if starttime.minute%time_level else time_level)
    while t < endtime:
        timeline.append(str(t.day)+'日'+(str(t.hour).zfill(2)+':'+str(t.minute//time_level*time_level).zfill(2)))
        t=t+datetime.timedelta(minutes=time_level)
    fdaytime=(starttime.hour*60+starttime.minute)//time_level+ (1 if starttime.minute%time_level else 0)
    daytime=60*24//time_level

    return {'starttime':starttime,'str_starttime':str_starttime,'endtime':endtime,'str_endtime':str_endtime,'timeline':timeline,'fdaytime':fdaytime,'daytime':daytime,'time_level':time_level}


def douyu():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    ret = session.query(DouyuModel).filter(sqlalchemy.and_(
        DouyuModel.rid==int(roomidframe.get()),
        DouyuModel.create_time.between(starttimeframe.get(),endtimeframe.get())
        )).all()
    return ret,ret[0].nn

def huya():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    ret = session.query(HuyaModel).filter(sqlalchemy.and_(
        HuyaModel.profileRoom==int(roomidframe.get()),
        HuyaModel.create_time.between(starttimeframe.get(),endtimeframe.get())
        )).all()
    print(len(ret))
    # for r in ret:
    #     print(r.nick)
    return ret,ret[0].nick
def egame():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    ret = session.query(EgameModel).filter(sqlalchemy.and_(
        EgameModel.anchor_id==int(roomidframe.get()),
        EgameModel.create_time.between(starttimeframe.get(),endtimeframe.get())
        )).all()
    return ret,ret[0].anchor_name
def bilibiliLive():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    ret = session.query(BilibiliLiveModel).filter(sqlalchemy.and_(
        BilibiliLiveModel.roomid==int(roomidframe.get()),
        BilibiliLiveModel.create_time.between(starttimeframe.get(),endtimeframe.get())
        )).all()
    return ret,ret[0].uname






def clickMe():
    file_path = filedialog.asksaveasfilename(defaultextension = '.xlsx')
    for p,d in platformdict.items():
        if platformChosen.get()==p:
            ret=d()
            data=ret[0]
            title = ret[1]
    print(file_path,starttimeframe.get(),endtimeframe.get())
    print(title,len(data))
    if len(data)==0:
        message = messagebox.showinfo(title='错误',message='未能获取到数据')
        # pass
    else:
        wb = openpyxl.Workbook()
        name= '%s_%s_%s-%s'%(platformChosen.get(),roomidframe.get(),starttimeframe.get(),endtimeframe.get())
        ws = wb.create_sheet(name.replace(':','_'))
        
        keys=[]
        for k,v in vars(data[0]).items():
            keys.append(k)
        ws.append(keys)

        for d in data:
            value = []
            for v in vars(d).items():
                value.append(str(v[-1]))
            ws.append(value)
        wb.save(file_path)


        timedata = GetTimeline(starttimeframe.get(),endtimeframe.get(),15)
        timeline=timedata['timeline']
        values=[0]*len(timedata['timeline'])
        i=0
        while i < len(data):
            if data[i].create_time.day-timedata['starttime'].day==0:
                seq = (data[i].time_scale//timedata['time_level'])-timedata['fdaytime']
                # print(seq,i)
            else:
                seq = data[i].time_scale//timedata['time_level'] - timedata['fdaytime']+(data[i].create_time.day-timedata['starttime'].day)*timedata['daytime']
            try:
                if platformChosen.get() == '虎牙':
                    values[seq]=data[i].totalCount
                if platformChosen.get() == '斗鱼':
                    values[seq]=data[i].ol
                if platformChosen.get() == '企鹅':
                    values[seq]=data[i].online
                if platformChosen.get() == 'B站直播':
                    values[seq]=data[i].online
            except:
                pass
            try:
                if values[seq-1]==0 and values[seq]!=0 and values[seq-2]!=0:
                    values[seq-1]=values[seq-2]
            except:
                pass
            
            # print(values)
            i+=1
        line = Line(title,"%s_%s"%(starttimeframe.get(),endtimeframe.get()),width=1920,height=1080)
        line.add(title,timedata['timeline'],values,area_opacity=0.4,is_lable_show=False)
        # print()
        line.render(file_path[:-5]+'.html')
        message = messagebox.showinfo(title='成功',message='已保存')


platformNow = StringVar()
platformNow.set('未选择')

def chosePlatform(*args):
    platformNow.set(platformChosen.get())
    print(platformNow)

platform = StringVar()
platformChosen = ttk.Combobox(root,width =12,textvariable=platform,state='readonly')
platformChosen['values'] = ('斗鱼','虎牙','企鹅','B站直播')
platformChosen.current(0)
platformChosen.bind("<<ComboboxSelected>>",chosePlatform)


starttimeframe= Entry(root)
endtimeframe = Entry(root)
roomidframe = Entry(root)

# ttk.Label(root,textvariable=platformNow).pack()
platformdict={
    '斗鱼':douyu,
    '虎牙':huya,
    '企鹅':egame,
    'B站直播':bilibiliLive,
}


action = Button(root,text='保存',command=clickMe)




ttk.Label(root,text='选择直播平台',width=12).pack()
platformChosen.pack()
ttk.Label(root,text='输入房间号').pack()
roomidframe.pack()
ttk.Label(root,text='输入开始时间（例：%s）'%today).pack()
starttimeframe.pack()
ttk.Label(root,text='输入结束时间（例：%s）'%today).pack()
endtimeframe.pack()
action.pack()



root.mainloop()