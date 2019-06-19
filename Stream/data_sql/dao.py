from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, func
from sqlalchemy import Integer, BIGINT, Boolean
from sqlalchemy import String, TEXT
from sqlalchemy import DateTime, TIMESTAMP, DATE, TIME
from sqlalchemy import Index, UniqueConstraint
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool
import datetime


ENGINE = create_engine(
    'mysql+pymysql://root:nice.tv520@120.27.151.217:3306/kts_database?charset=utf8mb4',
    # 'mysql+pymysql://root:nice.tv520@localhost:3306/kts_database?charset=utf8mb4',
    # 'mysql+pymysql://root:yangchen@localhost:3306/kts_database?charset=utf8mb4',
    max_overflow=10,
    pool_size=50,
    pool_timeout=30,
    pool_recycle=3600,
    # echo=True,
    # poolclass=NullPool,
)
base = declarative_base()
def create_db():  # 创建表
    base.metadata.create_all(ENGINE)  # 就是将继承的Base的类的所有的表都创建，创建到ENGINE数据库，就上上面那个mysql+pymysql数据库

def drop_db():  # 删除表
    base.metadata.drop_all(ENGINE)

# 实体——内容类型实体，如微博话题，斗鱼直播间
class tb_content_type(base):
    # 表属性
    __tablename__ ='tb_content_type_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    content_type_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='内容分类id（例如一期节目为一个内容）')  # 整数，默认主键，自增
    content_type_name = Column(String(255), nullable=False, comment='内容类型名称')
    content_type_level = Column(Integer, comment='权限等级')  # 字符串
    content_type_level_desc = Column(String(255), comment='权限等级描述')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer,comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer,comment='编辑用户的id')
    sys_deletime =  Column(TIMESTAMP, comment='删除时间')
    sys_deletor =  Column(Integer,comment='删除用户的id')
    sys_status =  Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 实体——内容实体，如xxx微博话题，KPL秋季赛直播，godlie节目
class tb_content(base):
    # 表属性
    __tablename__ ='tb_content_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    content_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='内容id（例如一期节目为一个内容）')  # 整数，默认主键，自增
    content_name = Column(String(255), nullable=False, comment='内容名称')
    content_type_id = Column(Integer, comment='内容类型id')
    content_level = Column(Integer, comment='权限等级')  # 字符串
    content_level_desc = Column(String(255), comment='权限等级描述')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer,comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer,comment='编辑用户的id')
    sys_deletime =  Column(TIMESTAMP, comment='删除时间')
    sys_deletor =  Column(Integer,comment='删除用户的id')
    sys_status =  Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 实体——内容媒体流/播放源，如微博主页，KPL斗鱼直播间
class tb_content_stream(base):
    # 表属性
    __tablename__ ='tb_content_stream_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    content_stream_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='内容媒体流/播放源id（例如KPL斗鱼直播间）')  # 整数，默认主键，自增
    content_stream_name = Column(String(255), comment='媒体流名称')
    # content_stream_uid = Column(String(50), nullable=False, comment='url请求的固定参数，例如微博id，多参数,隔开')
    content_id = Column(Integer, nullable=False, comment='内容id')
    content_stream_plat_id = Column(Integer, nullable=False, comment='平台id')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 实体——平台渠道
class tb_platform(base):
    # 表属性
    __tablename__ ='tb_plat_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    plat_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='平台id')  # 整数，默认主键，自增
    plat_name = Column(String(255), nullable=False, comment='平台名称')
    plat_desc = Column(String(255), comment='平台描述')
    plat_type_id = Column(Integer, comment='平台类型id')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 实体——api公式表
class tb_api_pattern(base):
    # 表属性
    __tablename__ = 'tb_api_pattern_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    api_pattern_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='api公式id')  # 整数，默认主键，自增
    api_pettern_url = Column(String(255), comment='api公式')
    api_pattern_plat_id = Column(Integer, comment='平台id')
    api_pattern_content_type_id = Column(Integer, nullable=False, comment='内容类型id')
    api_pattern_inter = Column(String(255), comment='对应程序接口')
    api_pattern_inter_func = Column(String(255), comment='对应程序接口函数')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 实体——实际请求api
class tb_api(base):
    # 表属性
    __tablename__ = 'tb_api_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    api_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='api id')  # 整数，默认主键，自增
    api_pattern_id = Column(Integer, nullable=False, comment='api公式id')
    api_content_stm_id = Column(Integer, nullable=False, comment='内容媒体流id')
    api_url = Column(String(255), comment='api实际请求url')
    api_url_id = Column(String(50), comment='api实际请求url的id')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 实体——任务
class tb_task(base):
    # 表属性
    __tablename__ ='tb_task_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    task_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='任务id')  # 整数，默认主键，自增
    task_api_id = Column(Integer, nullable=False, comment='api的id')
    task_level_id = Column(Integer, nullable=False, comment='任务等级')
    task_origintime = Column(TIME, nullable=False, server_default='00:00:00',comment='任务时间原点')
    task_priority = Column(Integer, server_default='100', comment='任务优先级')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 实体——任务等级
class tb_taskLevel(base):
    # 表属性
    __tablename__ ='tb_task_level_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    task_level_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='任务等级id')  # 整数，默认主键，自增
    task_level_timescale = Column(Integer, nullable=False, comment='任务时间刻度，单位s')
    task_level_priority = Column(Integer, server_default='100', comment='任务优先级')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 报表——百度指数
class rp_baiduIndex(base):
    # 表属性
    __tablename__ ='rp_baidu_index_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    rp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='百度指数报表id')  # 整数，默认主键，自增
    rp_keyword = Column(String(50), nullable=False, comment='关键词')
    rp_content_stm_id = Column(Integer, nullable=False, comment='媒体流ID')
    rp_date = Column(DATE, comment='指数日期')
    rp_index_all = Column(Integer, comment='百度指数双端')
    rp_index_pc = Column(Integer, comment='百度指数PC')
    rp_response = Column(TEXT, comment='请求返回json')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 报表——微博用户
class rp_weiboUser(base):
    # 表属性
    __tablename__ = 'rp_weibo_user_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    rp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='微博用户报表id')  # 整数，默认主键，自增
    rp_uid = Column(String(50), nullable=False, comment='微博用户id')
    rp_uname = Column(String(255),comment='微博用户名')
    rp_content_stm_id = Column(Integer, nullable=False, comment='媒体流ID')
    rp_status_num = Column(Integer, comment='微博状态数')
    rp_fan_num = Column(Integer, comment='粉丝数')
    rp_follow_num = Column(Integer, comment='关注数')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 报表——微博用户状态
class rp_weiboUserStatus(base):
    # 表属性
    __tablename__ = 'rp_weibo_user_status_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    rp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='微博用户状态报表id')  # 整数，默认主键，自增
    rp_status_id = Column(String(50), nullable=False, comment='微博状态id')
    rp_uid = Column(String(50), nullable=False, comment='微博用户id')
    rp_uname = Column(String(255), comment='微博用户名')
    rp_content_stm_id = Column(Integer, nullable=False, comment='媒体流ID')
    rp_status_text = Column(TEXT(), comment='状态内容')
    rp_repost_num = Column(Integer, comment='转发数')
    rp_comment_num = Column(Integer, comment='评论数')
    rp_like_num = Column(Integer, comment='点赞数')
    rp_publish_time = Column(String(255), comment='发文时间')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 报表——微博超话
class rp_weiboSuperIndex(base):
    # 表属性
    __tablename__ = 'rp_weibo_super_index_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    rp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='微博超话报表id')  # 整数，默认主键，自增
    rp_spid = Column(String(50), nullable=False, comment='微博超话id')
    rp_spname = Column(String(255), comment='超话名称')
    rp_content_stm_id = Column(Integer, nullable=False, comment='媒体流ID')
    rp_rank = Column(String(50), comment='分区排名')
    rp_read_num = Column(Integer, comment='阅读数')
    rp_status_num = Column(Integer, comment='帖子数')
    rp_fan_num = Column(Integer, comment='粉丝数')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 报表——斗鱼
class rp_douyu(base):
    # 表属性
    __tablename__ = 'rp_douyu_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    rp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='斗鱼直播间报表id')
    rp_uid = Column(String(50), nullable=False,comment='用户ID')
    rp_uname = Column(String(255), comment='用户昵称')
    rp_content_stm_id = Column(Integer, nullable=False, comment='媒体流ID')
    rp_rid = Column(Integer, comment='房间号')
    rp_rname = Column(String(255), comment='房间标题')
    rp_ol_num = Column(Integer, comment='在线人数')
    rp_cid1 = Column(Integer, comment='大分区id')
    rp_cid2 = Column(Integer, comment='游戏分区id')
    rp_cid3 = Column(Integer, comment='小分区id')
    rp_iv = Column(String(255), comment='颜值区')
    rp_url = Column(String(255), comment='直播间网址')
    rp_c2url = Column(String(255), comment='游戏分区网址')
    rp_c2name = Column(String(255), comment='游戏分区名')
    rp_od = Column(String(255), comment='主播认证')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 报表——egame
class rp_egame(base):
    # 表属性
    __tablename__ = 'rp_egame_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    rp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='egame直播间报表id')
    rp_uid = Column(String(50), nullable=False, comment='用户ID')
    rp_uname = Column(String(255), comment='用户昵称')
    rp_content_stm_id =  Column(Integer, nullable=False, comment='媒体流ID')
    rp_rname = Column(String(255),comment='房间标题')
    rp_ol_num = Column(Integer,comment='在线人数')
    rp_fan_num = Column(Integer, comment='粉丝数')
    rp_appid = Column(String(255),comment='游戏分区id')
    rp_appname = Column(String(255),comment='游戏分区名')
    rp_city = Column(String(255),comment='城市')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 报表——虎牙
class rp_huya(base):
    # 表属性
    __tablename__ = 'rp_huya_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    rp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='虎牙直播间报表id')
    rp_uid = Column(String(50), nullable=False, comment='用户ID')
    rp_uname = Column(String(255), comment='用户昵称')
    rp_content_stm_id = Column(Integer, nullable=False, comment='媒体流ID')
    rp_rid = Column(Integer, comment='房间号')
    rp_rname = Column(String(255), comment='房间标题')
    rp_ol_num = Column(Integer, comment='在线人数')
    rp_gid = Column(Integer, comment='游戏分区id')
    rp_gname = Column(String(255), comment='游戏分区名')
    rp_introduction = Column(String(255), comment='房间简介')
    rp_recommend_status = Column(String(255), comment='推荐状态')
    rp_recommend_tag = Column(String(255), comment='推荐标签')
    rp_channel = Column(String(255), comment='频道')
    rp_live_channel = Column(String(255), comment='直播频道')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

# 报表——b站直播
class rp_bilibiliUserLive(base):
    # 表属性
    __tablename__ = 'rp_bilibili_user_live_list'
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    # 专属字段
    rp_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, comment='b站直播间报表id')
    rp_uid = Column(String(50),comment='用户ID')
    rp_uname = Column(String(255),comment='用户昵称')
    rp_content_stm_id = Column(Integer, nullable=False, comment='媒体流ID')
    rp_rid = Column(Integer, comment='房间号')
    rp_rname = Column(String(255),comment='房间标题')
    rp_ol_num = Column(Integer,comment='在线人数')
    rp_area1_id = Column(String(255), comment='大分区id')
    rp_area1_name = Column(String(255),comment='大分区')
    rp_area2_id = Column(String(255), comment='游戏分区id')
    rp_area2_name = Column(String(255),comment='游戏分区名')
    rp_short_id = Column(String(255),comment='短id')
    # 共有字段
    sys_createtime = Column(TIMESTAMP, nullable=False, server_default=func.now(), comment='创建时间')
    sys_creator = Column(Integer, comment='创建用户的id')
    sys_edittime = Column(TIMESTAMP, comment='编辑时间')
    sys_editor = Column(Integer, comment='编辑用户的id')
    sys_deletime = Column(TIMESTAMP, comment='删除时间')
    sys_deletor = Column(Integer, comment='删除用户的id')
    sys_status = Column(Boolean, nullable=False, server_default='1', comment='状态值，1有效0无效')

if __name__=='__main__':
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    create_db()
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