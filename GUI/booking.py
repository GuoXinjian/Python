import pymysql,datetime,openpyxl,os,sqlalchemy

# TO DO
# 1. 每个小时查询本小时范围内应该发送的邮件
# 2. 查询内容： 用户，任务
# 3. 生成 用户_日期.xlsx 每一个任务创建一个sheet
# 4. 发送邮件




db = pymysql.connect("120.27.151.217",port=3306,user="root",password="nice.tv520",database="KTS",charset='utf8mb4')

cursor = db.cursor()


filePath = os.path.dirname(__file__)



def appendData(tableName,data,td=None):
    if not td:
        td = datetime.date.today()
    print(td)
    try:
        wb = openpyxl.load_workbook(filePath+'\\%s.xlsx'%td)
    except:
        print('创建新文件')
        wb = openpyxl.Workbook()
    # try:
    #     ws = wb[tableName]
    # except:
    ws = wb.create_sheet(tableName)
    for d in data:
        ws.append(d)
    wb.save(filePath+'\\%s.xlsx'%td)
    




def getKeys(tableName):#获取所有字段
    sql = 'show columns from %s'%tableName
    keys = []
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for key in results:
            keys.append(key[0])
    except:
        print('查无此表')
    return keys

def getInfo(arg:dict,tableName:str,keys=['*',],startDate=None,endDate=None,startTime=0,endTime=24):
    

    if len(keys)==1 and keys[0]=='*':
        keys = getKeys(tableName)
    results = [keys,]

    if not startDate:
        startDate = datetime.date.today()
        endDate = startDate+datetime.timedelta(days=1)
        #print(startDate,endDate)
    elif not endDate:
        endDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")+datetime.timedelta(days=1)
        endDate = endDate.strftime("%Y-%m-%d")
        print(endDate)

    k = ''
    for key in keys:
        k+=key+','

    sql = "select %s from %s where %s='%s' and create_time between '%s' and '%s' and time_scale between '%s' and '%s'"
    
    startTime = int(startTime) * 60
    endTime = int(endTime) * 60
    
    try:
        print(sql%(k[:-1],tableName,arg[0],arg[1],startDate,endDate,startTime,endTime))
        cursor.execute(sql%(k[:-1],tableName,arg[0],arg[1],startDate,endDate,startTime,endTime))
        results += cursor.fetchall()
        print(results)
    except Exception as e:
        print(e)

    return results
i=0
startDate = '2019-03-06'
while i<9:
    res = getInfo(['rid','100'],'douyu' ,startDate=startDate)
    appendData('douyu',res,td=startDate)

    res = getInfo(['anchor_id','605976197'],'egame' ,startDate=startDate)
    appendData('egame',res,td=startDate)

    res = getInfo(['uid','1560182545'],'huya' ,startDate=startDate)
    appendData('huya',res,td=startDate)

    startDate = datetime.datetime.strptime(startDate, "%Y-%m-%d")+datetime.timedelta(days=1)
    startDate = startDate.strftime("%Y-%m-%d")

    print(startDate)

    i+=1