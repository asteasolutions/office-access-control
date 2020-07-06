import sqlalchemy as sal
from sqlalchemy import create_engine


class DBConnection(object):
    #Connecting to database and printing names of tables
    engine = sal.create_engine("mssql+pyodbc://SA:password@localhost/CentaurEventTestCopy?driver=ODBC+Driver+17+for+SQL+Server")
    conn = engine.connect()
    
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        pass



