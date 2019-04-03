#coding=utf-8
import pymysql

db = pymysql.connect("localhost","root","guo3625202123","kol_info",charset='utf8mb4')

def streaminsert(tableid,streamdata):
    
    #print(streamdata)
    cursor = db.cursor()
    sql="INSERT INTO %s (roomid, userid, username, title, hot_index, game) VALUES ('%s','%s','%s','%s','%s','%s')"
    
    i = 0
    
    while i < len(streamdata[0]):
        data = (tableid,streamdata[0][i],streamdata[1][i],pymysql.escape_string(streamdata[2][i]),pymysql.escape_string(streamdata[3][i]),streamdata[4][i],streamdata[5][i])
        #print(data)
        cursor.execute(sql % data)
        i += 1
    db.commit()
    