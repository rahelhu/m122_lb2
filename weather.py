#author: Rahel Hüppi
#date: 25.03.2024
#version: 1.1
#description: A weather-app that runs with an API.

import requests

api_url = 'https://api.openweathermap.org/data/2.5/weather?lat=47.3744&lon=8.541&appid=85871cf84915b59ab767d9ae89395ae1'
response = requests.get(api_url)

if response.status_code == requests.codes.ok:
    #print(response.text)
    data = response.json()

    #main
    main = data['weather'][0]['main']

    #Temperatur
    tempKelvin = data['main']['temp']
    tempCelsius = tempKelvin - 273.15
    tempCelsius = round(tempCelsius, 2)

    #main, feels_like, temp_min, temp_max, humidity, visibility, speed (wind)
    #sunrise, sunset (unix)

    print("main:", main)
    print("Temperatur (in °C):", tempCelsius)
else:
    print("Error:", response.status_code, response.text)

