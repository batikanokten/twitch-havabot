import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather" #Current Weather Data
appid = "...API KEY..." # Get api key from https://openweathermap.org/ 


def weather(city):
    response = requests.get(url, params={"q": city, "appid": appid}) #Add params to url
    text = response.text
    data = json.loads(text)

    #Get info from json
    try:
        city_name = data["name"]
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
    except KeyError as e:
        return "Error:", data["message"]
        exit()

    #convert kelvin to celsius
    celsius = temperature - 273.15
    output = "Şehir: " + city_name + ", " + "Hava Durumu: " + description + ", " + "Sıcaklık: " + str(round(celsius,2)) + "°C" + ", " + "Nem: " + str(humidity) + "%" + ", " + "Rüzgar: " + str(wind) + "m/s"

    return output


if __name__ == "__main__":
    print(weather(input("City: "))) #For testing