#author: Rahel Hüppi
#date: 08.04.2024
#version: 1.1
#description: A weather-app that runs with an API.

import requests
import json
import datetime
import configparser

# load config.cfg
config = configparser.ConfigParser()
config.read('config.cfg')

# Access configuration settings
api_url = config.get('API', 'url')
api_key = config.get('API', 'key')
latitude = config.get('LOCATION', 'latitude')
longitude = config.get('LOCATION', 'longitude')
file_path = config.get('OUTPUT', 'filePath')

# Creating the full API URL
# f is for f-string: put variable-values directly into the string
api_url_full = f"{api_url}?lat={latitude}&lon={longitude}&appid={api_key}"



response = requests.get(api_url_full)

if response.status_code == requests.codes.ok:
    #print(response.text)
    data = response.json()

    #main
    city = data['name']
    country = data['sys']['country']
    main = data['weather'][0]['main']

    #Temperatur
    tempKelvin = data['main']['temp']
    temp = round(tempKelvin - 273.15, 1)

    feels_likeKelvin = data['main']['feels_like']
    feels_like = round(feels_likeKelvin - 273.15, 1)

    temp_minKelvin = data['main']['temp_min']
    temp_min = round(temp_minKelvin - 273.15, 1)

    temp_maxKelvin = data['main']['temp_max']
    temp_max = round(temp_maxKelvin - 273.15, 1)


    #other information
    humidity = data['main']['humidity'] #in %
    visibility = data['visibility'] #in m
    windSpeed = data['wind']['speed'] #in m/s


    sunriseUnix = data['sys']['sunrise'] #in Unix-Time
    sunrise = datetime.datetime.fromtimestamp(sunriseUnix) #convert to datetime object
    sunrise = sunrise.strftime("%H:%M:%S") #convert time in string
    

    sunsetUnix = data['sys']['sunset'] #in Unix-Time
    sunset = datetime.datetime.fromtimestamp(sunsetUnix)
    sunset = sunset.strftime("%H:%M:%S")
    

    # create Python-object 
    data = {
        "main": main,
        "temp": temp,
        "feels_like": feels_like,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "humidity": humidity,
        "visibility": visibility,
        "windSpeed": windSpeed,
        "sunrise": sunrise,
        "sunset": sunset,
    }

    # convert into JSON:
    jsonData = json.dumps(data, indent=2)


    #write in JSON-File
    datei = open('data.json','w') #w = write
    datei.write(jsonData)
    datei.close()

else:
    print("Error:", response.status_code, response.text)

