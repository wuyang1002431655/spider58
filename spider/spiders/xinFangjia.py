import scrapy
from .startUrls import startUrls
from spider.items import XinfangItem
class xinFangjia(scrapy.Spider):

    name = 'xinFangjia'
    start_urls=startUrls()
    start_urls=start_urls.getXinfangUrls()

    def parse(self, response):
        # with open('/Users/wuyang/HBuilderProjects/YuJia/index.html','w') as f:
        #     f.write(response.body.decode('utf-8'))
        #     f.close()
        item = XinfangItem()
        xinfangDIV=response.xpath('''//div[@class="key-list imglazyload"]/div[1]''')
        i=1
        while len(xinfangDIV) !=0:
            pClass=xinfangDIV.xpath('''a[2]/p[1]/@class''').extract()
            print(pClass)
            if pClass[0]=='price':#注意pClass是list，这点太坑了，之前没加[0]，判断全跑else
                xinFangPrice=xinfangDIV.xpath(''' a[2]/p[@class='price']//text()''').extract()
                flag=''
                for iii in xinFangPrice:
                    flag=flag+iii.strip()
                xinFangPrice=flag
            else:
                xinFangPrice=xinfangDIV.xpath(''' a[2]/p[2]//text()''').extract()
                flag=''
                for iii in xinFangPrice:
                    flag=flag+iii.strip()
                xinFangPrice=flag
            item['xinfangPrice']=xinFangPrice
            print(item['xinfangPrice'])
            xinfangName=xinfangDIV.xpath(''' div[1]/a[1]/h3[1]/span/text()  ''').extract()
            item['xinfangName']=xinfangName
            print(item['xinfangName'])
            i=i+1
            flag=''' //div[@class="key-list imglazyload"]/div[''' +str(i) +''']'''
            xinfangDIV=response.xpath(flag)
            yield item
        print(i)
        pass

'''
拆出楼盘板块的所有div，迭代这些div，拆出楼盘名称和价格，注意价格有总价，均价，周边均价
如果售价待定，那售价字段显示的是手机号
'''