import scrapy
from .startUrls import startUrls
from spider.items import SpiderItem
import pymysql
class xinfangSpider(scrapy.Spider):
    def __init__(self):
        self.connect=pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='wuyang1996920',
            db='spider58',
        )
        self.cursor=self.connect.cursor()#sql操作不应该放在spider里面
    name = 'xinfangSpider'
    start_urls=startUrls()
    start_urls=start_urls.getCityUrls()

    def parse(self, response):
        item=SpiderItem()
        cityUrl=response.xpath("/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[9]/a/@href").extract()
        cityUrl=response.urljoin(cityUrl[0])
        item['cityUrl']=cityUrl
        sql="SELECT cityID FROM city WHERE cityUrl=%s"
        self.cursor.execute(sql,response.url)
        cityID=self.cursor.fetchall()
        cityID=cityID[0][0]
        item['cityID']=cityID
        sql="SELECT cityChineseName FROM city WHERE cityUrl=%s"
        self.cursor.execute(sql,response.url)
        cityChineseName=self.cursor.fetchall()
        cityChineseName=cityChineseName[0][0]
        item['cityChineseName']=cityChineseName
        sql = "SELECT cityEnglishName FROM city WHERE cityUrl=%s"
        self.cursor.execute(sql, response.url)
        cityEnglishName = self.cursor.fetchall()
        cityEnglishName=cityEnglishName[0][0]
        item['cityEnglishName'] = cityEnglishName
        yield item