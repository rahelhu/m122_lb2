#author: Rahel Hüppi
#date: 08.04.2024
#version: 1.1
#description: A weather-app that runs with an API.

import requests
import json
import datetime

api_url = 'https://api.openweathermap.org/data/2.5/weather?lat=47.3744&lon=8.541&appid=85871cf84915b59ab767d9ae89395ae1'
response = requests.get(api_url)

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
    visibility = data['visibility']  #in m
    windSpeed = data['wind']['speed'] #in m/s


    sunriseUnix = data['sys']['sunrise'] #in Unix-Time
    sunrise = datetime.datetime.fromtimestamp(sunriseUnix) #convert to datetime object
    sunrise = sunrise.strftime("%H:%M:%S") #convert time in string
    

    sunsetUnix = data['sys']['sunset'] #in Unix-Time
    sunset = datetime.datetime.fromtimestamp(sunsetUnix)
    sunset = sunset.strftime("%H:%M:%S")
    

    # create Python-object 
    data = {
        #"city": city,
        #"country": country,
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
    print (jsonData)


    #write in JSON-File
    datei = open('data.json','w') #w = write
    datei.write(jsonData)

else:
    print("Error:", response.status_code, response.text)

