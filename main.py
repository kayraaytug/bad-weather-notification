import requests
import time
from win11toast import toast

API_KEY = "YOUR_API_KEY"


def main():

    response = requests.get("http://api.weatherapi.com/v1/forecast.json?key=" + API_KEY + "&q=Istanbul&days=1&aqi=no&alerts=no")
    response_json = response.json()

    #   locationTime = response_json['location']['localtime']
    #   currentWeather = response_json['current']['condition']['text']
    #   currentIcon = response_json['current']['condition']['icon']
    currentTemp = response_json['current']['temp_c']
    currentCountry = response_json['location']['name']

    daily_will_it_rain = response_json['forecast']['forecastday'][0]['day']['daily_will_it_rain']
    daily_chance_of_rain = response_json['forecast']['forecastday'][0]['day']['daily_chance_of_rain']
    daily_will_it_snow = response_json['forecast']['forecastday'][0]['day']['daily_will_it_snow']
    daily_chance_of_snow = response_json['forecast']['forecastday'][0]['day']['daily_chance_of_snow']

    if daily_will_it_rain > 0:
        toast(f'RAIN WARNING !! ', f'%{daily_chance_of_rain} will rain. {round(currentTemp)}°C')

    if daily_will_it_snow > 0:
        toast(f'SNOW WARNING !! ', f'%{daily_chance_of_snow} will snow. {round(currentTemp)}°C')


if __name__ == "__main__":
    toast('SCRIPT IS WORKING!!')
    while True:
        main()
        time.sleep(1800)
