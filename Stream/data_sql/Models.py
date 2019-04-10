from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Index, UniqueConstraint
from sqlalchemy.orm import sessionmaker, scoped_session
import datetime


ENGINE = create_engine(
    'mysql+pymysql://root:nice.tv520@120.27.151.217:3306/KTS?charset=utf8mb4',
    max_overflow=0,
    pool_size=10,
    pool_timeout=30,
    pool_recycle=-1,
    echo=True,
)
base = declarative_base()

class tasklistModel(base):
    __tablename__ = 'tasklist'

    sys_id = Column(Integer,primary_key=True,autoincrement=True)
    level = Column(Integer)
    id = Column(String(255))
    platform = Column(String(255),nullable=False)


class DouyuModel(base):
    __tablename__ = 'douyu'
    sys_id = Column(Integer,primary_key=True,autoincrement=True)
    rid = Column(Integer,comment='房间号')
    rn = Column(String(255),comment='房间标题')
    uid = Column(Integer,comment='用户ID')
    nn = Column(String(255),comment='用户昵称')
    cid1 = Column(String(255),comment='大分区id')
    cid2 = Column(String(255),comment='游戏分区id')
    cid3 = Column(String(255),comment='小分区id')
    iv = Column(String(255),comment='颜值区')
    ol = Column(Integer,comment='在线人数')
    url = Column(String(255),comment='直播间网址')
    c2url = Column(String(255),comment='游戏分区网址')
    c2name = Column(String(255),comment='游戏分区名')
    od = Column(String(255),comment='主播认证')
    create_time = Column(DateTime,comment='创建时间')
    time_scale =  Column(Integer,comment='时间刻度')
    sys_level =  Column(Integer,comment='时间等级')


class EgameModel(base):
    __tablename__ = 'egame'
    sys_id = Column(Integer,primary_key=True,autoincrement=True)
    title = Column(String(255),comment='房间标题')
    anchor_id = Column(Integer,comment='用户ID')
    anchor_name = Column(String(255),comment='用户昵称')
    online = Column(Integer,comment='在线人数')
    appid = Column(String(255),comment='游戏分区id')
    appname = Column(String(255),comment='游戏分区名')
    city = Column(String(255),comment='城市')
    fans_count = Column(String(255),comment='粉丝数')
    create_time = Column(DateTime,comment='创建时间')
    time_scale =  Column(Integer,comment='时间刻度')
    sys_level =  Column(Integer,comment='时间等级')


class HuyaModel(base):
    __tablename__ = 'huya'
    sys_id = Column(Integer,primary_key=True,autoincrement=True)
    gameFullName = Column(String(255),comment='游戏分区名')
    gid = Column(String(255),comment='游戏分区id')
    totalCount = Column(Integer,comment='在线人数')
    roomName = Column(String(255),comment='房间标题')
    nick = Column(String(255),comment='用户昵称')
    introduction = Column(String(255),comment='房间简介')
    recommendStatus = Column(String(255),comment='推荐状态')
    recommendTagName = Column(String(255),comment='推荐标签')
    uid = Column(Integer,comment='用户ID')
    channel = Column(Integer,comment='频道')
    liveChannel = Column(Integer,comment='直播频道')
    profileRoom = Column(Integer,comment='房间号')
    create_time = Column(DateTime,comment='创建时间')
    time_scale =  Column(Integer,comment='时间刻度')
    sys_level =  Column(Integer,comment='时间等级')

class BilibiliLiveModel(base):
    __tablename__ = 'bilibiliLive'
    sys_id = Column(Integer,primary_key=True,autoincrement=True)
    uid = Column(Integer,comment='用户ID')
    title = Column(String(255),comment='房间标题')
    roomid = Column(Integer,comment='房间号')
    uname = Column(String(255),comment='用户昵称')
    online = Column(Integer,comment='在线人数')
    areaName = Column(String(255),comment='大分区')
    area = Column(String(255),comment='大分区id')
    area_v2_name = Column(String(255),comment='游戏分区名')
    area_v2_id = Column(String(255),comment='游戏分区id')
    short_id = Column(String(255),comment='短id')
    create_time = Column(DateTime,comment='创建时间')
    time_scale =  Column(Integer,comment='时间刻度')
    sys_level =  Column(Integer,comment='时间等级')


class UserInfo(base):
    __tablename__ ='user_info'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 整数，默认主键，自增
    name = Column(String(32), index=True, nullable=False)  # 字符串
    extra = Column(String(32), unique=True)  # 字符串
def create_db():  # 创建表
    base.metadata.create_all(ENGINE)  # 就是将继承的Base的类的所有的表都创建，创建到ENGINE数据库，就上上面那个mysql+pymysql数据库

def drop_db():  # 删除表
    base.metadata.drop_all(ENGINE)

if __name__=='__main__':
    # Session = sessionmaker(bind=ENGINE)
    # session = Session()

    # obj = tasklistModel()
    # obj.level = 222
    # obj.id = 'aaaa'
    # obj.platform = 'dddd'
    # session.add(obj)
    # session.commit()
    # session.close()

    # ret1 = session.query(HuyaModel).filter_by(uid = 367138632).all()
    # filter_by(HuyaModel.uid=367138632).all()
    # for r in ret1:
    #     print(r.nick,r.totalCount)


    sbj = tasklistModel()
    print(dir(sbj))
    print(sbj.__dict__)