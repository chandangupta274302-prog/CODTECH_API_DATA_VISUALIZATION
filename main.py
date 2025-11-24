import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
CITY = "Gorakhpur"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()

dates, temps, humidity = [], [], []

for item in data['list']:
    dates.append(item['dt_txt'])
    temps.append(item['main']['temp'])
    humidity.append(item['main']['humidity'])

df = pd.DataFrame({
    "Date": dates,
    "Temperature (°C)": temps,
    "Humidity (%)": humidity
})

print(df.head())

plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Temperature (°C)"])
plt.xticks(rotation=90)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Forecast - Gorakhpur")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 5))
plt.plot(df["Date"], df["Humidity (%)"])
plt.xticks(rotation=90)
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")
plt.title("Humidity Forecast - Gorakhpur")
plt.tight_layout()
plt.show()
