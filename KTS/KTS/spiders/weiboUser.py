# -*- coding: utf-8 -*-
import scrapy,json
from KTS.items import *


class WeibouserSpider(scrapy.Spider):
    name = 'weiboUser'
    allowed_domains = ['m.weibo.cn']
    start_urls = ['https://m.weibo.cn/api/container/getIndex?containerid=1005051681029540']

    # def start_requests(self):
    #     return [scrapy.Request('https://weibo.cn/xxxxx', callback=self.parse)]

    def parse(self, response):
        #print(response.body)
        data = json.loads(response.body)
        user_data = data['data']['userInfo']
        item = WeiboUserItem()
        item['user_id']=user_data['id']
        item['user_name']=user_data['screen_name']
        item['user_url']=user_data['profile_url']
        item['statuses_count']=user_data['statuses_count']
        item['verified']=user_data['verified']
        item['verified_type']=user_data['verified_type']
        item['verified_reason']=user_data['verified_reason']
        item['description']=user_data['description']
        item['gender']=user_data['gender']
        item['followers_count']=user_data['followers_count']
        item['follow_count']=user_data['follow_count']
        item['avatar_hd']=user_data['avatar_hd']
        print(item)
        yield item