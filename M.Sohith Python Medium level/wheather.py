import requests

def get_weather(city_name):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def get_forecast(city_name):
    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_current_weather(data):
    if data['cod'] == 200:
        print(f"Current weather in {data['name']}:")
        print(f"Weather: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("City not found. Please try again.")

def display_forecast(data):
    if data['cod'] == '200':
        print(f"5-day weather forecast for {data['city']['name']}:")
        for forecast in data['list']:
            print(f"Date: {forecast['dt_txt']}")
            print(f"Weather: {forecast['weather'][0]['description']}")
            print(f"Temperature: {forecast['main']['temp']}°C")
            print(f"Humidity: {forecast['main']['humidity']}%")
            print(f"Wind Speed: {forecast['wind']['speed']} m/s")
            print("-------------------------")
    else:
        print("City not found. Please try again.")

def main():
    city_name = input("Enter city name: ")
    current_weather_data = get_weather(city_name)
    forecast_data = get_forecast(city_name)

    print("\n===== Current Weather =====")
    display_current_weather(current_weather_data)

    print("\n===== 5-Day Forecast =====")
    display_forecast(forecast_data)

if __name__ == "__main__":
    main()
