from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.engine.interfaces import Dialect
from sqlalchemy.orm import  relationship
from db import Database, Base, engine, sessionmaker

db = Database()

class City(Base):

    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    nm_city = Column(String(200))
    nm_state = Column(String(200))
    nu_long = Column(Float)
    nu_lat = Column(Float)
    sg_country = Column(String(4))

    def __repr__(self):
        return self.nm_city

    def __init__(self, id, nm_city, nm_state, nu_long, nu_lat, sg_country):
        self.id = id
        self.nm_city = nm_city
        self.nm_state = nm_state
        self.nu_long = nu_long
        self.nu_lat = nu_lat
        self.sg_country = sg_country

    @classmethod
    def create(cls):
        cls.__table__.create(engine, checkfirst=True)
                     
    def add(self):
        try:                
            Session = sessionmaker(bind=engine) 
            session = Session()
            session.add(self)
            session.commit()                     
        except Exception as inst:
            session.rollback() 
            print(type(inst))    # the exception instance
            print(inst.args)     # arguments stored in .args   
        return self.id            



class Forecast(Base):

    __tablename__ = 'forecast'    
    dt_mensage =  Column(Integer, primary_key=True)
    temp = Column(Float)
    feels_like = Column(Float)
    temp_min = Column(Float)
    temp_max = Column(Float)
    pressure = Column(Float)
    sea_level = Column(Float)
    grnd_level = Column(Float)
    humidity = Column(Float)
    temp_kf = Column(Float)
    dt_day = Column(Integer)
    dt_month = Column(Integer)
    dt_year = Column(Integer)
    dt_hour = Column(Integer)
    dt_min = Column(Integer)
    dt_sec = Column(Integer)
    wind_speed = Column(Float)
    wind_deg = Column(Float)
    wind_gust = Column(Float)
    visibility = Column(Float)
    pop = Column(Float)
    pod = Column(String(10))
    clouds = Column(Float)
    rain = Column(Float)
    snow = Column(Float)    
    id_city = Column(Integer, ForeignKey('city.id',  ondelete="cascade"))
    relationship('City', backref='city', cascade="all, delete", passive_deletes=True)     


    def __repr__(self):
        return f'Dt: {self.dt_mensage}'

    def __init__(self, dt_mensage,temp,feels_like,temp_min,temp_max,pressure,sea_level,grnd_level,humidity,temp_kf,dt_day,dt_month,dt_year,dt_hour,dt_min,dt_sec,wind_speed,wind_deg,wind_gust,visibility,pop,pod,clouds,rain,snow,city):
        self.dt_mensage = dt_mensage
        self.temp = temp
        self.feels_like = feels_like
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.pressure = pressure
        self.sea_level = sea_level
        self.grnd_level = grnd_level
        self.humidity = humidity
        self.temp_kf = temp_kf
        self.dt_day = dt_day
        self.dt_month = dt_month
        self.dt_year = dt_year
        self.dt_hour = dt_hour
        self.dt_min = dt_min
        self.dt_sec = dt_sec
        self.wind_speed = wind_speed
        self.wind_deg = wind_deg
        self.wind_gust = wind_gust
        self.visibility = visibility
        self.pop = pop
        self.pod = pod
        self.clouds = clouds
        self.rain = rain
        self.snow = snow
        self.id_city = city
        
    @classmethod
    def create(cls):
        cls.__table__.create(engine, checkfirst=True)
                     
    def add(self):
        try:                
            Session = sessionmaker(bind=engine) 
            session = Session()
            session.add(self)
            session.commit()                     
        except Exception as inst:
            session.rollback() 
            print(type(inst))   
            print(inst.args)    
        return self.dt_mensage            



class History(Base):

    __tablename__ = 'weather_history'
    dt_mensage =  Column(Integer, primary_key=True)
    temp = Column(Float)
    feels_like = Column(Float)
    pressure = Column(Float)
    humidity = Column(Float)
    dew_point = Column(Float)
    dt_day = Column(Integer)
    dt_month = Column(Integer)
    dt_year = Column(Integer)
    dt_hour = Column(Integer)
    dt_min = Column(Integer)
    dt_sec = Column(Integer)
    wind_speed = Column(Float)
    wind_deg = Column(Float)
    wind_gust = Column(Float)
    visibility = Column(Float)
    uvi = Column(Float)    
    clouds = Column(Float)      
    id_city = Column(Integer, ForeignKey('city.id',  ondelete="cascade"))
    relationship('City', backref='city', cascade="all, delete", passive_deletes=True)     


    def __repr__(self):
        return f'Dt: {self.dt_mensage}'

    def __init__(self, dt_mensage,temp,feels_like,pressure,humidity,dew_point,dt_day,dt_month,dt_year,dt_hour,dt_min,dt_sec,wind_speed,wind_deg,wind_gust,visibility,uvi,clouds,city):
        self.dt_mensage = dt_mensage
        self.temp = temp
        self.feels_like = feels_like                
        self.pressure = pressure      
        self.humidity  = humidity
        self.dew_point = dew_point
        self.dt_day = dt_day
        self.dt_month = dt_month
        self.dt_year = dt_year
        self.dt_hour = dt_hour
        self.dt_min = dt_min
        self.dt_sec = dt_sec
        self.wind_speed = wind_speed
        self.wind_deg = wind_deg
        self.wind_gust = wind_gust
        self.visibility = visibility
        self.uvi = uvi
        self.clouds = clouds
        self.id_city = city    


    @classmethod
    def create(cls):
        cls.__table__.create(engine, checkfirst=True)
                     
    def add(self):
        try:                
            Session = sessionmaker(bind=engine) 
            session = Session()
            session.add(self)
            session.commit()                     
        except Exception as inst:
            session.rollback() 
            print(type(inst))    
            print(inst.args)   
        return self.dt_mensage            
