from tkinter import *
from tkinter import ttk,filedialog
import time
import openpyxl
from Models import *
import sqlalchemy


root = Tk()
root.title('直播间数据查询下载')
root.geometry('300x200')
today = time.strftime('%Y-%m-%d',time.localtime(time.time()))
starttime=today
endtime = '2019-03-23'



def douyu():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    ret = session.query(DouyuModel).filter(sqlalchemy.and_(
        DouyuModel.rid==int(roomidframe.get()),
        DouyuModel.create_time.between(starttimeframe.get(),endtimeframe.get())
        )).all()
    return ret

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
    return ret
def egame():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    ret = session.query(EgameModel).filter(sqlalchemy.and_(
        EgameModel.anchor_id==int(roomidframe.get()),
        EgameModel.create_time.between(starttimeframe.get(),endtimeframe.get())
        )).all()
    return ret
def bilibiliLive():
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    ret = session.query(BilibiliLiveModel).filter(sqlalchemy.and_(
        BilibiliLiveModel.roomid==int(roomidframe.get()),
        BilibiliLiveModel.create_time.between(starttimeframe.get(),endtimeframe.get())
        )).all()
    return ret






def clickMe():
    file_path = filedialog.asksaveasfilename(defaultextension = '.xls')
    for p,d in platformdict.items():
        if platformChosen.get()==p:
            data=d()
    print(file_path,starttimeframe.get(),endtimeframe.get())
    print(len(data))
    if len(data)==0:
        message = messagebox.showinfo(title='错误',message='未能获取到数据')
    else:
        wb = openpyxl.Workbook()
        ws = wb.create_sheet('%s_%s_%s-%s'%(platformChosen.get(),roomidframe.get(),starttimeframe.get(),endtimeframe.get()))
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