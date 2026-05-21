"""
Real-Time Weather Dashboard
Author: Fatimah Agboola

A Python command-line weather dashboard using the Open-Meteo API.
Skills demonstrated:
- REST API integration
- JSON parsing
- Error handling
- User input validation
- Clean modular programming

No API key required.
"""

import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_coordinates(city: str):
    """Fetch latitude and longitude for a city using Open-Meteo geocoding."""
    try:
        response = requests.get(
            GEOCODING_URL,
            params={"name": city, "count": 1, "language": "en", "format": "json"},
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        if "results" not in data or not data["results"]:
            return None

        result = data["results"][0]
        return {
            "name": result.get("name"),
            "country": result.get("country"),
            "latitude": result.get("latitude"),
            "longitude": result.get("longitude"),
        }

    except requests.RequestException as error:
        print(f"Network error while finding location: {error}")
        return None


def get_weather(latitude: float, longitude: float):
    """Fetch current weather for the given coordinates."""
    try:
        response = requests.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
                "timezone": "auto",
            },
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    except requests.RequestException as error:
        print(f"Network error while fetching weather: {error}")
        return None


def interpret_weather_code(code: int) -> str:
    """Return a readable weather description from Open-Meteo weather codes."""
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
    }
    return weather_codes.get(code, "Unknown conditions")


def display_weather(location: dict, weather_data: dict) -> None:
    current = weather_data.get("current", {})

    print("\nWeather Dashboard")
    print("-" * 40)
    print(f"Location: {location['name']}, {location['country']}")
    print(f"Temperature: {current.get('temperature_2m')}°C")
    print(f"Humidity: {current.get('relative_humidity_2m')}%")
    print(f"Wind Speed: {current.get('wind_speed_10m')} km/h")
    print(f"Conditions: {interpret_weather_code(current.get('weather_code'))}")
    print("-" * 40)


def main() -> None:
    print("Real-Time Weather Dashboard")
    print("Type 'exit' to close the app.")

    while True:
        city = input("\nEnter a city: ").strip()

        if city.lower() == "exit":
            print("Goodbye.")
            break

        if not city:
            print("Please enter a valid city name.")
            continue

        location = get_coordinates(city)

        if location is None:
            print("City not found. Try a different location.")
            continue

        weather_data = get_weather(location["latitude"], location["longitude"])

        if weather_data is None:
            print("Could not retrieve weather data.")
            continue

        display_weather(location, weather_data)


if __name__ == "__main__":
    main()
