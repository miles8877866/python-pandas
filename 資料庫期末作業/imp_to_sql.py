import requests
import json
import pandas as pd
import pymysql

with open('C:\\Users\\as722\\Desktop\\資料庫\\資料庫期末作業\\data.json', encoding='utf-8') as jsonfile:
    list_of_dicts = json.load(jsonfile)
print
# list_of_dicts = r.json()

# print(type(r)) #test
# print(type(list_of_dicts))
# for i in list_of_dicts:
#     print(i["County"], i["PublishAgency"], i["PublishTime"])

spf = [i["特優5家"] for i in list_of_dicts]
name = [i["店名"] for i in list_of_dicts]
addr = [i["地址"] for i in list_of_dicts]
lev = [i["等級"] for i in list_of_dicts]

aqi_dict = {
    "SPF": spf,
    "NAME": name,
    "ADDR": addr,
    "LEV": lev
}
conn = pymysql.connect(host='localhost',port=3306,user='root',password='n226165528',db='db_demo',charset='utf8')
cursor = conn.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data) # 結果表明已經連線成功
for i in range(len(spf)):
    spf = aqi_dict['SPF'][i]
    name = aqi_dict['NAME'][i]
    addr = aqi_dict['ADDR'][i]
    lev = aqi_dict['LEV'][i]
    print(spf, name, addr, lev)
    cursor.execute("INSERT INTO db_demo.db_final(Special_five, name, address, level)VALUES('{0}','{1}','{2}', '{3}');".format(spf, name, addr, lev)) 
conn.commit() 
cursor.close() 
conn.close()

# df = pd.DataFrame(aqi_dict)
# df.to_csv("aqi.csv", index=False)
# with open("aqi.json", "w") as f:
#     json.dump(aqi_dict, f, ensure_ascii=False)

