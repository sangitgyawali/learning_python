# Weather App (using API)

import requests

def get_weather(city):
    api_key = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            condition = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            print(f"\n🌤️ Weather in {city.title()}:")
            print(f"🌡️ Temperature: {temp}°C")
            print(f"🌫️ Condition: {condition}")
            print(f"💧 Humidity: {humidity}%")
        else:
            print("❌ City not found!")

    except:
        print("⚠️ Could not fetch weather data.")

city = input("Enter city name: ")
get_weather(city)
