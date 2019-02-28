import scrapy

class weiboUser(scrapy.Spider):
    name='weiboUser'
    
    start_urls = [
        'https://m.weibo.cn/api/container/getIndex?containerid=1005051681029540'
    ]

    
    def parse(self,response):
        print(response.body)