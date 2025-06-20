import requests
import matplotlib.pyplot as plt
import seaborn as sns

# ✅ Public demo API key (for educational/testing use only)
API_KEY = '439d4b804bc8187953eb36d2a8c26a02'  # OpenWeatherMap free demo key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# 🔘 Cities to analyze
cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Pune', 'Jaipur', 'Hyderabad']

# 🔘 Store temperature and humidity data
temperatures = []
humidities = []

# 🔄 Fetch data for each city
for city in cities:
    complete_url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data['main']
        temperatures.append(main['temp'])
        humidities.append(main['humidity'])
    else:
        temperatures.append(None)
        humidities.append(None)

# 📊 Visualization with seaborn
sns.set(style="whitegrid")

# 🌡 Temperature Bar Plot
plt.figure(figsize=(10, 5))
sns.barplot(x=cities, y=temperatures, palette="coolwarm")
plt.title('City-wise Temperature (°C)', fontsize=14)
plt.xlabel('Cities')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 💧 Humidity Bar Plot
plt.figure(figsize=(10, 5))
sns.barplot(x=cities, y=humidities, palette="Blues_d")
plt.title('City-wise Humidity (%)', fontsize=14)
plt.xlabel('Cities')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
