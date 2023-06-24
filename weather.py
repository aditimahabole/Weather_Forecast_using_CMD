import argparse
import requests
import json
def show_weather_forecast(city_name):
    try:
        my_api_key = "50f26bffba7f4175167013c5c0db4a3f"
        base_url=f"http://api.openweathermap.org/data/2.5/weather?appid={my_api_key}&q={city_name}"
        response = requests.get(base_url)
        res = response.json()
        if res['cod'] == 200:
            weather_data = json.loads(response.text)
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            result = f'Weather forecast for : {city_name}\n'
            result += f'Temperature: {temperature} K\n'
            result += f'Humidity: {humidity}%'
            return result   
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        return f'HTTP Error !: {http_err}'
    except requests.exceptions.RequestException as err:
        return f'Some Error: {err}'
def use_command_line():
    parser = argparse.ArgumentParser(description='Weather Forecasting Tool')
    parser.add_argument('city',type=str,help='City name')
    try:
        args = parser.parse_args()
        city_name = args.city
        print(city_name)
        weather_forecast = show_weather_forecast(city_name)
        print("##################################")
        print(weather_forecast)
        print("##################################")
    except:
        print("Please enter a city name in the command line.")
    
if __name__ == '__main__':
    use_command_line()
# GitHub Copilot can assist with code completion when working with APIs.
# It can help suggest the appropriate API endpoints, query parameters, 
# and data structures based on the OpenWeatherMap API.
# Made by Aditi Mahabole and Molshree Sharma

