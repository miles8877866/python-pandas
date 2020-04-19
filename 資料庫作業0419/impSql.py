import importlib,sys
importlib.reload(sys)
import pandas as pd
 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
 
DB_CONNECT_STRING = 'mysql+pymysql://root:n226165528@localhost/db_demo?charset=utf8'
engine = create_engine(DB_CONNECT_STRING, echo=True)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()
 
csv_data = pd.read_csv('hw0419.csv',encoding='utf-8')
print(csv_data.shape)
pd.io.sql.to_sql(frame=csv_data,name='score_data',con=engine,index=False,if_exists='append')
