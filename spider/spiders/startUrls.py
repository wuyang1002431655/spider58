import pymysql

class startUrls(object):
    def __init__(self):
        self.connect=pymysql.connect(
            host='localhost',
            port=3306,
            db='spider58',
            user='root',
            passwd='wuyang1996920'
        )
        self.cursor=self.connect.cursor()
    '''
    返回url的list
    '''
    def getCityUrls(self):
        sql="SELECT cityUrl FROM city"#返回全部url
        # sql="SELECT cityUrl FROM city LIMIT 5"#仅返回五个url用于测试
        # sql="SELECT cityUrl FROM city WHERE 442<cityID"#仅返回442以后的数据用于测试
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        flag=list()
        for i in range(len(results)):
            for j in range(len(results[i])):
                flag.append(results[i][j])
        return flag

    def getXinfangUrls(self):
        # sql="SELECT cityUrl FROM xinfang WHERE cityID=2"#仅返回一个url用于测试
        sql = "SELECT cityUrl FROM xinfang"
        self.cursor.execute(sql)
        results=self.cursor.fetchall()
        xinfangUrl=list()
        for i in range(len(results)):
            for j in range(len(results[i])):
                xinfangUrl.append(results[i][j])

        return xinfangUrl
