import sqlalchemy as sal
from sqlalchemy import create_engine
from configparser import ConfigParser

class DBConnection(object):
    config = ConfigParser()
    config.read('config.ini')
    #Connecting to database and printing names of tables
    con_string = "mssql+pyodbc://{}:{}@{}/{}?driver={}".format(config['database']['user'], config['database']['pass'], config['database']['host'], config['database']['DBName'], config['database']['driver'])
    engine = sal.create_engine(con_string)
    conn = engine.connect()
    
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        pass



