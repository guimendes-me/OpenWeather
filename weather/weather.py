import requests
import json
from datetime import datetime, timezone, timedelta
from models import City, Forecast, History


#create models
History.create()
Forecast.create()
City.create()


#api parameters
API_KEY = '85c00ae97c1228ab59fb4aaeb941fe93'
CITY_ID = '3448433'
lat=-49.0
log=-22.0

def loadCity():
        with open('city.list.json', 'r', encoding="utf8") as json_file:
                data = json.load(json_file)
                for row in data:
                        city = City(row["name"], row["state"], row["coord"]["lon"], row["coord"]["lat"], row["country"])
                        city.add()
                        print(city)

def forecastAPI():
        response = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?id={CITY_ID}&appid={API_KEY}')
        if response.status_code == 200:
                json_list = (response.json())
                for json in json_list["list"]:                        
                        dt_value = datetime.strptime(json["dt_txt"], '%Y-%m-%d %H:%M:%S')                           
                        dt_mensage = json["dt"]
                        temp = json["main"]["temp"]
                        feels_like = json["main"]["feels_like"]
                        temp_min = json["main"]["temp_min"]
                        temp_max = json["main"]["temp_max"]
                        pressure = json["main"]["pressure"]
                        sea_level = json["main"]["sea_level"]
                        grnd_level = json["main"]["grnd_level"]
                        humidity = json["main"]["humidity"]
                        temp_kf = json["main"]["temp_kf"]
                        dt_day = dt_value.day                
                        dt_month = dt_value.month
                        dt_year = dt_value.year
                        dt_hour = dt_value.hour
                        dt_min = dt_value.minute
                        dt_sec = dt_value.second
                        wind_speed = json["wind"]["speed"]
                        wind_deg = json["wind"]["deg"]
                        wind_gust = json["wind"]["gust"]
                        visibility = json["visibility"]
                        pop = json["pop"]
                        pod = json["sys"]["pod"]
                        clouds = json["clouds"]["all"]
                        rain = None
                        snow = None
                        city = CITY_ID
                        weather =  Forecast(dt_mensage,temp,feels_like,temp_min,temp_max,pressure,sea_level,grnd_level,humidity,temp_kf,dt_day,dt_month,dt_year,dt_hour,dt_min,dt_sec,wind_speed,wind_deg,wind_gust,visibility,pop,pod,clouds,rain,snow,city)
                        print(weather, dt_value)
                        weather.add()

def historyAPI(days):

        #get time in unix format
        dt = datetime.now() - timedelta(days=days)
        timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
        time=timestamp.__round__()

        response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={log}&dt={time}&appid={API_KEY}')
        json_list = response.json()        
        
        if response.status_code == 200:
                for json in json_list["hourly"]:                
                        local_time = datetime.fromtimestamp(json["dt"] )   
                        str_value = local_time.strftime("%Y-%m-%d %H:%M:%S.%f")
                        dt_value = datetime.strptime(str_value, "%Y-%m-%d %H:%M:%S.%f") 
                        dt_mensage = json["dt"]                
                        temp = json["temp"]
                        feels_like = json["feels_like"]                
                        pressure = json["pressure"]      
                        humidity  = json["humidity"]
                        dew_point = json["dew_point"]
                        dt_day = dt_value.day                
                        dt_month = dt_value.month
                        dt_year = dt_value.year
                        dt_hour = dt_value.hour
                        dt_min = dt_value.minute
                        dt_sec = dt_value.second
                        wind_speed = json["wind_speed"]
                        wind_deg = json["wind_deg"]
                        wind_gust = json["wind_gust"]
                        visibility = json["visibility"]
                        uvi = json["uvi"]
                        clouds = json["clouds"]
                        city = CITY_ID                               
                        history = History(dt_mensage,temp,feels_like,pressure,humidity,dew_point,dt_day,dt_month,dt_year,dt_hour,dt_min,dt_sec,wind_speed,wind_deg,wind_gust,visibility,uvi,clouds,city)
                        print(history)
                        history.add()                      


for i in range(0,5):
        historyAPI(i)

