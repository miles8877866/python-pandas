import pymysql

db = pymysql.connect("localhost", "root", "n226165528", "db_demo")

cursor = db.cursor()
# use execute to implement the sql seelect
cursor.execute("select VERSION()")

data = cursor.fetchone()
print("Database Version : %s" %data)

def oper():
    #sql = """ALTER TABLE db_final ADD add_code int after name;"""
    #sql = """update db_final set add_code = substr(address, 1, 3)"""
    #sql = """SET SQL_SAFE_UPDATES=0"""
    #sql = """ALTER TABLE db_final ADD city carchar(40) after name;"""
    #sql = """update db_final set city = substr(address, 4, 3)"""
#     sql = """select
# 	address, substring(address, 7,instr(address, '區')-6) "區", add_code
# from db_final"""
    # sql = """create table addr_final (add_code int, dist varchar(20));"""
#     sql = """INSERT addr_final (add_code, dist)
# select distinct add_code, substring(address, 4,instr(address, '區')-3)
# FROM db_final;"""
    #sql = """create table level_h (name varchar(20), add_code int, address varchar(20), level int);"""
    #sql = """create table level_h (name varchar(20), add_code int, address varchar(20), level int);"""
#     insert level_h(Special_five, name, add_code, dist, road, level) 
# select Special_five, name, add_code, dist, road, level from final_view 
# where level = '特優' order by Special_five
# """
    #sql = """create table level_m (name varchar(20), add_code int, address varchar(50), level varchar(10));"""
    #sql = """create table level_L (name varchar(20), add_code int, address varchar(50), level varchar(10));"""
#     sql = """-- insert level_L(name, add_code, address, level)
# -- select name, add_code, address, level from db_final	where level = "良" """
#     sql = """create view fi_h_view as SELECT final_view.* FROM final_view INNER JOIN level_h 
# ON final_view.level = level_h.level and final_view.name =  level_h.name
# ORDER BY level_h.level"""
#     sql = """create view test_view as SELECT a.* FROM final_view as a INNER JOIN  final_view as b 
# ON a.level = "優" and a.name =  b.name
# ORDER BY a.Special_five"""
#     sql = """create view Low_view as SELECT a.* FROM final_view as a INNER JOIN  final_view as b 
# ON a.level = "良" and a.name =  b.name
# ORDER BY a.Special_five"""
    sql = """"""
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            id = row[0]
            name = row[1]
            
            print("id=%s, name = %s" % (id, name))
        db.commit()
    except:
        db.rollback()


if __name__ == "__main__":
    oper()
    db.close()