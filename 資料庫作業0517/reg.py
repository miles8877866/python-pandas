import urllib.parse
import requests
import pymysql
import json
import time

def ADD_TABLE(): 
    con = pymysql.connect(host = 'localhost',user = 'root',passwd = 'n226165528',db = 'db_demo')
    cursor = con.cursor()

    # cursor.execute("DROP TABLE IF EXISTS db_uv") # 習慣性
# sql = """CREATE TABLE db_uv (
#        `County` VARCHAR(20),
#        `PublishAgency` VARCHAR(100),
#        `PublishTime` VARCHAR(200),
#        `SiteName` varchar(20),
#        `UVI` VARCHAR(20),
#        `WGS84Lat` varchar(20),
#        `WGS84Lon` varchar(20)
#        )
#        """
# cursor.execute(sql) # 根據需要建立一個表格
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data) # 結果表明已經連線成功
    for i in json_obj:
        print("County:", i["County"])
        print("PA:", i["PublishAgency"])
        print("PT:", i["PublishTime"])
        print("PT:", i["SiteName"])
        print("UVI:", i["UVI"])
        print("PT:", i["WGS84Lat"])
        print("PT:", i["WGS84Lon"])
        print('---')
        cursor.execute("INSERT INTO db_uv (County, PublishAgency, PublishTime, SiteName, UVI, WGS84Lat, WGS84Lon) VALUES (%s, %s, %s, %s, %s, %s, %s)", (i["County"], i["PublishAgency"], i["PublishTime"], i["SiteName"], i["UVI"], i["WGS84Lat"], i["WGS84Lon"]))
    cursor.execute("CREATE TABLE reg_uv AS (SELECT DISTINCT * FROM db_uv)")#刪除重複資料
    cursor.execute("DELETE FROM db_uv")    
    cursor.execute("INSERT INTO db_uv (SELECT * FROM reg_uv)")
    cursor.execute("DROP TABLE reg_uv")
    cursor.execute("CREATE or replace VIEW uv_view (D, County, uv_avg) AS SELECT substring(PublishTime, 1, 10), County, AVG(UVI) FROM db_uv group by substring(PublishTime, 1, 10), County")
    con.commit()
    con.close()
headers = { 'User-Agent' : 'User-Agent:Mozilla/5.0' }
url = 'http://opendata.epa.gov.tw/webapi/Data/UV/?$orderby=PublishTime%20desc&$skip=0&$top=1000&format=json'
data1 = urllib.request.Request(url , headers = headers )
response = urllib.request.urlopen(data1).read() 
# json_obj = str(response, 'utf-8')
json_obj = json.loads(response.decode('utf-8'))


def saver():
    number = json_obj
    file_name = 'C:\\Users\\as722\\Desktop\\資料庫作業0517\\test.py' #儲存為json 格式
    with open(file_name,'w') as file_object:
        json.dump(number,file_object)

def timer(n):
    while True:
        saver()
        ADD_TABLE()
        time.sleep(n)
# main
if __name__ == "__main__":

    timer(3600)
