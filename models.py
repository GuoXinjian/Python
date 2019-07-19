from sqlalchemy import Integer,Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time,os

try:
    path='KPL%s.db'%time.strftime('%Y%m%d')
    os.remove(path)
except:
    pass
# 创建对象的基类:
Base = declarative_base()


# 初始化数据库连接:
engine = create_engine('sqlite:///KPL%s.db?check_same_thread=False'%time.strftime('%Y%m%d'))

class maindata(Base):
    __tablename__ = 'maindata'

    id=Column(Integer,primary_key=True)
    bluedragon = Column(Integer)
    bluetower  = Column(Integer)
    bluepoint  = Column(Integer)
    blueeco    = Column(String(20))
    bluetyrant = Column(Integer)
    bluedarktyrant = Column(Integer)
    blueoverlord = Column(Integer)
    reddragon  = Column(Integer)
    redtower   = Column(Integer)
    redpoint   = Column(Integer)
    redeco     = Column(String(20))

class eco(Base):
    __tablename__ = 'eco'
    id=Column(Integer,primary_key=True)
    blueeco1   = Column(Integer)
    blueeco2   = Column(Integer)
    blueeco3   = Column(Integer)
    blueeco4   = Column(Integer)
    blueeco5   = Column(Integer)
    redeco1    = Column(Integer)
    redeco2    = Column(Integer)
    redeco3    = Column(Integer)
    redeco4    = Column(Integer)
    redeco5    = Column(Integer)

class match(Base):
    __tablename__ = 'match'
    id=Column(Integer,primary_key=True)
    blueplayer1 = Column(String(20))
    blueplayer2 = Column(String(20))
    blueplayer3 = Column(String(20))
    blueplayer4 = Column(String(20))
    blueplayer5 = Column(String(20))
    redplayer1  = Column(String(20))
    redplayer2  = Column(String(20))
    redplayer3  = Column(String(20))
    redplayer4  = Column(String(20))
    redplayer5  = Column(String(20))
    bluehero1   = Column(String(20))
    bluehero2   = Column(String(20))
    bluehero3   = Column(String(20))
    bluehero4   = Column(String(20))
    bluehero5   = Column(String(20))
    redhero1    = Column(String(20))
    redhero2    = Column(String(20))
    redhero3    = Column(String(20))
    redhero4    = Column(String(20))
    redhero5    = Column(String(20))

class kda(Base):
    __tablename__ = 'kda'
    id=Column(Integer,primary_key=True)
    bluekill1   = Column(Integer)
    bluedeath1 = Column(Integer)
    blueassist1 = Column(Integer)
    bluekill2   = Column(Integer)
    bluedeath2  = Column(Integer)
    blueassist2 = Column(Integer)
    bluekill3   = Column(Integer)
    bluedeath3  = Column(Integer)
    blueassist3 = Column(Integer)
    bluekill4   = Column(Integer)
    bluedeath4  = Column(Integer)
    blueassist4 = Column(Integer)
    bluekill5   = Column(Integer)
    bluedeath5  = Column(Integer)
    blueassist5 = Column(Integer)
    redkill1    = Column(Integer)
    reddeath1   = Column(Integer)
    redassist1  = Column(Integer)
    redkill2    = Column(Integer)
    reddeath2   = Column(Integer)
    redassist2  = Column(Integer)
    redkill3    = Column(Integer)
    reddeath3   = Column(Integer)
    redassist3  = Column(Integer)
    redkill4    = Column(Integer)
    reddeath4   = Column(Integer)
    redassist4  = Column(Integer)
    redkill5    = Column(Integer)
    reddeath5   = Column(Integer)
    redassist5  = Column(Integer)
    

class winrate(Base):
    __tablename__ = 'winrate'
    id=Column(Integer,primary_key=True)
    time = Column(String(20))
    blue = Column(String(20))
    red  = Column(String(20))


