import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your actual API key
API_KEY = '4bbbaefe2948dda272bd7273faef1cbd'
CITY = 'Delhi'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch data from API
response = requests.get(URL)
data = response.json()

# Parse data
forecast_list = data['list']
weather_data = {
    'datetime': [],
    'temperature': [],
    'humidity': [],
    'weather': []
}

for forecast in forecast_list:
    weather_data['datetime'].append(forecast['dt_txt'])
    weather_data['temperature'].append(forecast['main']['temp'])
    weather_data['humidity'].append(forecast['main']['humidity'])
    weather_data['weather'].append(forecast['weather'][0]['main'])

# Convert to DataFrame
df = pd.DataFrame(weather_data)
df['datetime'] = pd.to_datetime(df['datetime'])

# ------------------------
# 📊 Visualization Dashboard
# ------------------------

sns.set(style="darkgrid")

# Plot 1: Temperature over time
plt.figure(figsize=(12, 6))
plt.plot(df['datetime'], df['temperature'], marker='o', color='coral')
plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Humidity over time
plt.figure(figsize=(12, 6))
sns.lineplot(x='datetime', y='humidity', data=df, marker='o', color='skyblue')
plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 3: Weather condition count
plt.figure(figsize=(8, 5))
sns.countplot(x='weather', data=df, palette='viridis')
plt.title(f"Weather Condition Frequency in {CITY}")
plt.xlabel("Weather Condition")
plt.ylabel("Count")
plt.tight_layout()
plt.show()