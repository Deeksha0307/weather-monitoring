import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import time
import warnings
warnings.filterwarnings("ignore")

# Constants
API_KEY = '65d5ccb5be4e036473205385f3b129cf'  # Replace with your OpenWeatherMap API key
CITIES = ['Mumbai', 'Delhi', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
ALERT_THRESHOLD = 35
FETCH_INTERVAL = 300  

# Ask user for temperature unit preference
def get_temperature_unit_preference():
    print("Select temperature unit:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == '1':
        return 'metric', '°C'
    elif choice == '2':
        return 'imperial', '°F'
    elif choice == '3':
        return None, 'K'  # Kelvin is default
    else:
        print("Invalid choice! Defaulting to Celsius.")
        return 'metric', '°C'

# Fetch current weather data for a city
def fetch_weather_data(city, unit):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units={unit}" if unit else f"{BASE_URL}?q={city}&appid={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()

        # Check if the API call was successful
        if response.status_code == 200:
            return data
        else:
            print(f"Error fetching data for {city}: {data.get('message', 'Unknown error')}")
            return None
    except Exception as e:
        print(f"Exception occurred while fetching data for {city}: {e}")
        return None

# Process and structure the weather data
def process_weather_data(data, temp_unit):
    if data:
        try:
            return {
                'city': data['name'],
                'main': data['weather'][0]['main'],
                'temp': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
                'dt': datetime.utcfromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S'),
                'temp_unit': temp_unit
            }
        except KeyError as e:
            print(f"Missing expected key in data: {e}")
            return None
    return None

# Calculate daily weather summary with rollups and aggregates
def calculate_daily_aggregates(df):
    df['date'] = pd.to_datetime(df['dt']).dt.date
    daily_summary = df.groupby('date').agg(
        avg_temp=('temp', 'mean'),
        max_temp=('temp', 'max'),
        min_temp=('temp', 'min'),
        dominant_condition=('main', lambda x: x.mode()[0])
    ).reset_index()
    return daily_summary

# Check if any alert thresholds are exceeded
def check_alerts(df):
    alerts = df[df['temp'] > ALERT_THRESHOLD]
    if not alerts.empty:
        print("\n---ALERT---")
        print(f"High temperature alert for the following cities:\n{alerts[['city', 'temp']]}")
        print("---END ALERT---\n")

# Plot weather trends (daily average, max, min temperatures)
def plot_weather_trends(df):
    df.plot(x='date', y=['avg_temp', 'max_temp', 'min_temp'], kind='line')
    plt.title('Weather Trends')
    plt.show()

# Main execution loop
if __name__ == "__main__":
    # Get user preference for temperature unit
    temp_unit, temp_unit_symbol = get_temperature_unit_preference()

    # Continuously fetch data every 5 minutes
    while True:
        weather_data_list = []

        # Fetch and process weather data for all cities
        for city in CITIES:
            weather_data = fetch_weather_data(city, temp_unit)
            processed_data = process_weather_data(weather_data, temp_unit_symbol)
            if processed_data:
                weather_data_list.append(processed_data)

        # If we have valid weather data, proceed
        if weather_data_list:
            df = pd.DataFrame(weather_data_list)
            print("\n---Current Weather Data---")
            print(df[['city', 'main', 'temp', 'feels_like', 'humidity', 'wind_speed', 'dt', 'temp_unit']])

            # Calculate daily summary and check alerts
            daily_summary = calculate_daily_aggregates(df)
            print("\n---Daily Weather Summary---")
            print(daily_summary)

            check_alerts(df)

            # Plot the weather trends
            plot_weather_trends(daily_summary)
        else:
            print("No valid weather data available.")

        # Wait for the next fetch interval
        print(f"\nWaiting for {FETCH_INTERVAL // 60} minutes before fetching the next update...\n")
        time.sleep(FETCH_INTERVAL)