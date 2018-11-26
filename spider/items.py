# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cityChineseName=scrapy.Field()
    cityEnglishName=scrapy.Field()
    cityUrl=scrapy.Field()
    cityID=scrapy.Field()
    pass
class XinfangItem(scrapy.Item):
    xinfangCityID=scrapy.Field()
    xinfangCityName=scrapy.Field()
    xinfangName=scrapy.Field()
    xinfangPrice=scrapy.Field()
