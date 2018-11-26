# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql.cursors

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class city58Pipeline(object):
    def __init__(self):
        self.connect=pymysql.connect(
            host='localhost',
            port=3306,
            db='spider58',
            user='root',
            passwd='wuyang1996920',
        )
        self.cursor=self.connect.cursor()
    def process_item(self,item,spider):
        if spider.name!='city58':
            return item
        '''
        用mysql存储
        '''
        sql="INSERT INTO city (cityUrl,cityChineseName,cityEnglishName) VALUES (%s,%s,%s)"
        self.cursor.execute(sql,(item['cityUrl'],item['cityChineseName'],item['cityEnglishName']))
        self.connect.commit()
        print('数据已入库')
        return item

class xinfangPipeline(object):
    def __init__(self):
        self.connect=pymysql.connect(
            port=3306,
            user='root',
            passwd='wuyang1996920',
            db='spider58',
            host='localhost',
        )
        self.cursor=self.connect.cursor()

    def process_item(self,item,spider):
        if spider.name!='xinfangSpider':
            return item
        sql="INSERT INTO xinfang (cityID,cityChineseName,cityEnglishName,cityUrl) VALUES(%s,%s,%s,%s)"
        self.cursor.execute(sql,(item['cityID'],item['cityChineseName'],item['cityEnglishName'],item['cityUrl']))
        self.connect.commit()
        print('新房链接已入库')
        return item
class xinfangPricePipeline(object):
    def __init__(self):
        self.connect=pymysql.connect(
            port=3306,
            user='root',
            passwd='wuyang1996920',
            db='spider58',
            host='localhost',#密码都懒得屏蔽，没有入侵价值
        )
        self.cursor=self.connect.cursor()
    def process_item(self,item,spider):
        if spider.name!='xinFangjia':
            return item
        sql="INSERT INTO xinfangPrice (xinfangName,xinfangPrice) VALUES(%s,%s)"
        self.cursor.execute(sql,(item['xinfangName'],item['xinfangPrice']))
        self.connect.commit()
        print('数据已入库')
        return  item