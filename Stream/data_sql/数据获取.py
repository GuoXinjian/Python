import time,datetime,os
from multiprocessing import Pool
import openpyxl
from Models import *
import sqlalchemy
import pymysql
from pyecharts import Line
import pyecharts,pyecharts_snapshot,jupyter_echarts_pypkg,jinja2

file_path=os.getcwd()


def GetTimeline(start,end,time_level):
    time_level=time_level



    starttime=datetime.datetime.strptime(start,'%Y-%m-%d')
    starttime=starttime+datetime.timedelta(hours=5)



    endtime=datetime.datetime.strptime(end,'%Y-%m-%d')
    endtime=endtime+datetime.timedelta(hours=5)

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



def douyu(rid,str_starttime,str_endtime):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    ret = session.query(DouyuModel).filter(sqlalchemy.and_(
        DouyuModel.rid==int(rid),
        DouyuModel.create_time.between(str_starttime,str_endtime)
        )).all()
    return ret,ret[0].nn

def huya(rid,str_starttime,str_endtime):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    ret = session.query(HuyaModel).filter(sqlalchemy.and_(
        HuyaModel.profileRoom==int(rid),
        HuyaModel.create_time.between(str_starttime,str_endtime)
        )).all()
    print(len(ret))
    # for r in ret:
    #     print(r.nick)
    return ret,ret[0].nick
def egame(rid,str_starttime,str_endtime):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    ret = session.query(EgameModel).filter(sqlalchemy.and_(
        EgameModel.anchor_id==int(rid),
        EgameModel.create_time.between(str_starttime,str_endtime)
        )).all()
    return ret,ret[0].anchor_name
def bilibiliLive(rid,str_starttime,str_endtime):
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    ret = session.query(BilibiliLiveModel).filter(sqlalchemy.and_(
        BilibiliLiveModel.roomid==int(rid),
        BilibiliLiveModel.create_time.between(str_starttime,str_endtime)
        )).all()
    return ret,ret[0].uname

platformdict={
    '斗鱼':douyu,
    '虎牙':huya,
    '企鹅':egame,
    'B站直播':bilibiliLive,
}


def getdata(platform,rid,timedata):
    for p,d in platformdict.items():
        if platform==p:
            data=d(rid,timedata['str_starttime'],timedata['str_endtime'])
    if len(data[0])>0:        
        return data
def save(platform,data,timedata):
    title=data[1]
    wb = openpyxl.Workbook()
    name= '%s_%s_%s-%s'%(platform,title,timedata['str_starttime'],timedata['str_endtime'])
    ws=wb.create_sheet(name.replace(':','_'))
    keys=[]
    # print(data[0])
    for k,v in vars(data[0][0]).items():
        keys.append(k)
    ws.append(keys)
    for d in data[0]:
        value = []
        for v in vars(d).items():
            value.append(str(v[-1]))
        ws.append(value)
    wb.save(file_path+'\\'+name.replace(':','_')+'.xlsx')



    # timeline=timedata['timeline']
    values=[0]*len(timedata['timeline'])
    i=0
    while i < len(data[0]):
        if data[0][i].create_time.day-timedata['starttime'].day==0:
            seq = (data[0][i].time_scale//timedata['time_level'])-timedata['fdaytime']
            # print(seq,i)
        else:
            seq = data[0][i].time_scale//timedata['time_level'] - timedata['fdaytime']+(data[0][i].create_time.day-timedata['starttime'].day)*timedata['daytime']
        try:
            if platform == '虎牙':
                values[seq]=data[0][i].totalCount
            if platform == '斗鱼':
                values[seq]=data[0][i].ol
            if platform == '企鹅':
                values[seq]=data[0][i].online
            if platform == 'B站直播':
                values[seq]=data[0][i].online
        except:
            pass
        try:
            if values[seq-1]==0 and values[seq]!=0 and values[seq-2]!=0:
                values[seq-1]=values[seq-2]
        except:
            pass
        i+=1
    line = Line(platform+'-'+title,"%s_%s"%(timedata['str_starttime'],timedata['str_endtime']),width=1080,height=720)
    line.add(title,timedata['timeline'],values,area_opacity=0.4,is_lable_show=False)
    print('save'+timedata['str_starttime'])
    line.render(file_path+'\\'+name.replace(':','_')+'.html')

def main(start,end,platform,rid):
    timedata=GetTimeline(start,end,15)
    data=getdata(platform,rid,timedata)
    save(platform,data,timedata)

if __name__=='__main__':
    
    # strstart='2019-03-06'
    # start=datetime.datetime.strptime(strstart,'%Y-%m-%d')
    # end = start+datetime.timedelta(days=1)
    # pool=Pool(38)
    # for i in range(63):
    #     # main(start.strftime('%Y-%m-%d'),end.strftime('%Y-%m-%d'),'斗鱼',1863767)
    #     pool.apply_async(main,args=[start.strftime('%Y-%m-%d'),end.strftime('%Y-%m-%d'),'斗鱼',1863767])
    #     start=end
    #     end = start+datetime.timedelta(days=1)
    # pool.close()
    # pool.join()



    # strstart='2019-03-06'
    # start=datetime.datetime.strptime(strstart,'%Y-%m-%d')
    # end = start+datetime.timedelta(days=1)
    # pool=Pool(38)
    # print('douyu')
    # for i in range(63):
    #     # main(start.strftime('%Y-%m-%d'),end.strftime('%Y-%m-%d'),'企鹅',127935490)
    #     pool.apply_async(main,args=[start.strftime('%Y-%m-%d'),end.strftime('%Y-%m-%d'),'企鹅',127935490])
    #     start=end
    #     end = start+datetime.timedelta(days=1)
    # pool.close()
    # pool.join()



    # strstart='2019-03-06'
    # start=datetime.datetime.strptime(strstart,'%Y-%m-%d')
    # end = start+datetime.timedelta(days=1)
    # pool=Pool(38)
    # print('egame')
    # for i in range(63):
    #     # main(start.strftime('%Y-%m-%d'),end.strftime('%Y-%m-%d'),'虎牙',660002)
    #     pool.apply_async(main,args=[start.strftime('%Y-%m-%d'),end.strftime('%Y-%m-%d'),'虎牙',660002])
    #     start=end
    #     end = start+datetime.timedelta(days=1)
    # print('huya')
    # pool.close()
    # pool.join()


    strstart='2019-03-06'
    start=datetime.datetime.strptime(strstart,'%Y-%m-%d')
    end = start+datetime.timedelta(days=1)
    pool=Pool(38)
    for i in range(63):
        # main(start.strftime('%Y-%m-%d'),end.strftime('%Y-%m-%d'),'B站直播',906159)
        pool.apply_async(main,args=[start.strftime('%Y-%m-%d'),end.strftime('%Y-%m-%d'),'B站直播',21144080])
        start=end
        end = start+datetime.timedelta(days=1)
    print('bili')
    pool.close()
    pool.join()


