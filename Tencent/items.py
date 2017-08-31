# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # 职位名
    positionName = scrapy.Field()
    # 职位链接
    positionLink = scrapy.Field()
    # 职位类型
    positionType = scrapy.Field()
    # 招聘人数
    peopleNumber = scrapy.Field()
    # 工作地点
    workPosition = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()
