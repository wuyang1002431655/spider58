import scrapy
from spider.items import SpiderItem
import re
class city58(scrapy.Spider):
    name = 'city58'
    start_urls=['http://www.58.com/changecity.aspx']#请采集aspx静态页面，带js渲染的正在学习
    def parse(self, response):

        '''
        经测试，共有459个城市
        '''
        # cityUrls=response.xpath("/html/body/div[@class='topcity']/dl[@id='clist']/dd/a/@href").extract()#提取城市链接
        # cityNames=response.xpath("/html/body/div[@class='topcity']/dl[@id='clist']/dd/a/text()").extract()#提取城市名称
        citys=response.xpath("/html/body/div[@class='topcity']/dl[@id='clist']/dd/a")#提取城市信息
        item=SpiderItem()
        for city in citys:
            cityChineseName=city.xpath('text()').extract()#提取城市中文名称
            cityEnglishName=city.xpath('@onclick').extract()#提取城市英文名称
            pattern=re.compile("'(.*?)'")#抽取出的名字带有一对单引号，此问题暂未解决
            print(type(cityEnglishName))
            matcher = re.search(pattern, cityEnglishName[0])
            cityEnglishName=matcher.group()
            cityEnglishName=cityEnglishName[1:-1]#暂时用字符串切片解决
            cityUrl=city.xpath('@href').extract()[0]#提取城市链接
            cityUrl=response.urljoin(cityUrl)
            print(cityUrl)
            item['cityChineseName']=cityChineseName
            item['cityEnglishName'] = cityEnglishName
            item['cityUrl']=cityUrl
            yield item
