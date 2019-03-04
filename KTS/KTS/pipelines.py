# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class KtsPipeline(object):
    def process_item(self, item, spider):
        return item


class WeiboUserPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('132.232.77.200','root','guo3625202123','KTS_scrapy')
        self.cursor = self.conn.cursor()
    
    def process_item(self,item,spider):
        keys = ''
        values = ''
        #print(item['user_id'])
        for k,v in item.items():
            keys += "`" + k + "`,"
            values += "'" + pymysql.escape_string(str(v))+"',"
        sql="INSERT INTO %s (%s) VALUES (%s)"
        table = 'weiboUser'
        data = (table,keys[:-1],values[:-1])
        # print(sql,data)
        self.cursor.execute(sql % data)
        self.conn.commit()
        # user_id = item['user_id']
        # user_name = item['user_name']
        
    def close_spider(self,spider):
        self.conn.close()