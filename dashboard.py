import streamlit as st
import pandas as pd
import requests

st.title("Weather Data Visualization Dashboard (Gorakhpur)")

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

st.write(df)

st.subheader("Temperature Forecast Chart (Gorakhpur)")
st.line_chart(df.set_index("Date")["Temperature (°C)"])

st.subheader("Humidity Forecast Chart (Gorakhpur)")
st.line_chart(df.set_index("Date")["Humidity (%)"])
