import json

with open("weather.json", "r") as file:
    data = json.load(file)

temp = data['main']['temp']
humidity = data['main']['temp']
description = data['weather'][0]['description']

print(f"temp: {temp} \nhumidity: {humidity} \ndescription: {description}")
