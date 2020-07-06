import pyodbc
import sqlalchemy as sal
from sqlalchemy import create_engine

#Connecting to database and printing names of tables
engine = sal.create_engine("mssql+pyodbc://sa:Strong_Password@localhost/CentaurEventTestCopy?driver=SQL+Server")
conn = engine.connect()
print(engine.table_names())