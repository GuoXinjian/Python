# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KtsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class WeiboUserItem(scrapy.Item):
    user_id = scrapy.Field()
    user_name = scrapy.Field()
    user_url = scrapy.Field()
    statuses_count = scrapy.Field()
    verified = scrapy.Field()
    verified_type = scrapy.Field()
    verified_reason = scrapy.Field()
    description = scrapy.Field()
    gender = scrapy.Field()
    followers_count = scrapy.Field()
    follow_count = scrapy.Field()
    avatar_hd = scrapy.Field()

    