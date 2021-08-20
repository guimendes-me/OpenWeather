from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import  database_exists, create_database
import logging

db = 'mysql'
host='127.0.0.1'
port=3306
database='weather'
user='root'
password='admxz.82'

Base = declarative_base()

if db == 'mysql':                                 
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}', echo=False, pool_size=200, max_overflow=300)    
    if not database_exists(engine.url):                
        print('Criando banco de dados')
        create_database(engine.url)     


class Config():

    def __init__(self, appname, db, host, port, database, user, password):
        self.appname = appname
        self.db = db
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password 
        
        if self.db == 'mysql':                        
            #self.engine = create_engine(f'{self.db}+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/scraper', echo=True)
            self.engine = engine
            if database_exists(self.engine.url):                
                pass
            else:
                logging.info('Criando banco de dados')
                create_database(self.engine.url)                             

class Database():

    def __init__(self):

        #database = Config(appname='blake', db='mysql', host='35.202.33.13', port=3306, database='blake', user='root', password='admxz.82')
        Session = sessionmaker(bind=engine)
        session = Session()                
        self.session =  session
        self.conn = engine.connect()
        
    def createmodels(self, models):
        for model in models:
            model.__table__.create(bind=engine, checkfirst=True)
            logging.info(f'Table {model.__tablename__} created')
                        