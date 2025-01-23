import requests
import os
import time

# Constants
API_KEY = "bd5e378503939ddaee76f12ad7a97608"  # Replace with your OpenWeatherMap API key
CITY = "Delhi"  # Replace with your city
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """Fetches weather data from OpenWeatherMap API."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Use metric for Celsius
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def send_notification(title, message):
    """Send a notification on macOS using osascript."""
    os.system(f"""osascript -e 'display notification "{message}" with title "{title}"'""")

if __name__ == "__main__":
    while True:
        try:
            weather_data = get_weather(CITY)
            if weather_data.get("cod") == 200:
                temp = weather_data["main"]["temp"]
                description = weather_data["weather"][0]["description"]
                message = f"Temperature: {temp}°C\nCondition: {description.capitalize()}"
                send_notification(f"Weather Update for {CITY}", message)
            else:
                send_notification("Weather Update Error", "Failed to fetch weather data.")
        except Exception as e:
            send_notification("Error", str(e))
        
        # Check every hour (3600 seconds)
        time.sleep(10)
