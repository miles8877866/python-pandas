import requests
import json
import pandas as pd
import pymysql

url = "http://opendata.epa.gov.tw/webapi/Data/UV/?$orderby=PublishTime%20desc&$skip=0&$top=1000&format=json"
r = requests.get(url, verify=False)
wbdata = requests.get(url).text
list_of_dicts = json.loads(wbdata)
# list_of_dicts = r.json()

# print(type(r)) #test
# print(type(list_of_dicts))
# for i in list_of_dicts:
#     print(i["County"], i["PublishAgency"], i["PublishTime"])

counties = [i["County"] for i in list_of_dicts]
PA = [i["PublishAgency"] for i in list_of_dicts]
PT = [i["PublishTime"] for i in list_of_dicts]
SN = [i["SiteName"] for i in list_of_dicts]
UVI = [i["UVI"] for i in list_of_dicts]
WGS84Lat = [i["WGS84Lat"] for i in list_of_dicts]
WGS84Lon = [i["WGS84Lon"] for i in list_of_dicts]

news = list_of_dicts

aqi_dict = {
    "County": counties,
    "PublishAgency": PA,
    "PublishTime": PT,
    "SiteName": SN,
    "UVI": UVI,
    "WGS84Lat": WGS84Lat,
    "WGS84Lon": WGS84Lon
}


# conn = pymysql.connect(host='localhost',port=3306,user='root',password='n226165528',db='db_demo',charset='utf8')

# cursor = conn.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Database version : %s " % data) # 結果表明已經連線成功
# cursor.execute("DROP TABLE IF EXISTS db_UV") # 習慣性
# sql = """CREATE TABLE db_UV (
#        `County` VARCHAR(20),
#        `PublishAgency` VARCHAR(100),
#        `PublishTime` VARCHAR(200),
#        `SiteName` varchar(20),
#        `UVI` VARCHAR(10) NOT NULL,
#        `WGS84Lat` varchar(20),
#        `WGS84Lon` varchar(20)
#        )
#        """
# cursor.execute(sql) # 根據需要建立一個表格

#print(r.status_code)

for n in aqi_dict: 
  county = n['County'] 
  PA = n['PublishAgency'] 
  PT = n['PublishTime'] 
  SN = n['SiteName']
  UVI = n['UVI']
  WGS84Lat = n['WGS84Lat']
  WGS84Lon = n['WGS84Lon'] 
  print(county, PA, PT, SN, UVI, WGS84Lat, WGS84Lon) 
#   cursor.execute("INSERT INTO db_demo.db_uv(County, PublishAgency, PublishTime, SiteName, UVI,WGS84Lat, WGS84Lon)VALUES('{0}','{1}','{2}', '{3}', '{4}', '{5}', '{6}');".format(county, PA, PT, SN, UVI, WGS84Lat, WGS84Lon)) 
# conn.commit() 
# cursor.close() 
# conn.close()

# df = pd.DataFrame(aqi_dict)
# df.to_csv("aqi.csv", index=False)
# with open("aqi.json", "w") as f:
#     json.dump(aqi_dict, f, ensure_ascii=False)

