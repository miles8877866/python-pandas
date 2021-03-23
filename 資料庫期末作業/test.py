import json
with open('C:\\Users\\as722\\Desktop\\資料庫\\資料庫期末作業\\data.json', encoding='utf-8') as jsonfile:
    list_of_dicts = json.load(jsonfile)
print(list_of_dicts)