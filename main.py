import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "2d530b302e7e040b63ba97532494a82c"
CITY = "Chennai"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()


wind_speed = response['main'] ['humidity']
humidity = response ['main'] ['humidity']
description = response['weather'] [0] ['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response ['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response ['timezone'])

print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind speed in {CITY}: {wind_speed}m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sun rises in {CITY} at {sunrise_time}local time.")
print(f"Sun set in {CITY} at {sunset_time}local time.")


print(response)
