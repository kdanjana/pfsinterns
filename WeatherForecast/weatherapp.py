import requests
import tkinter as tk
from tkinter import ttk, messagebox

# Function to fetch weather data from OpenWeatherMap API
def getWeatherData(apiKey, city):
    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
    completeURL = baseURL + "appid=" + apiKey + "&q=" + city
    response = requests.get(completeURL)
    return response.json()

# Function to handle button click event and update weather information
def fetchWeather():
    city = cityEntry.get()
    apiKey = "APIKEy"  # Replace with your OpenWeatherMap API key
    if city:
        weatherData = getWeatherData(apiKey, city)
        if weatherData.get("cod") != "404":
            try:
                # print(weatherData)
                y = weatherData["main"]
                currentTemperature = y["temp"]
                currentHumidity = y["humidity"]
                currentWindSpeed = weatherData["wind"]["speed"]
                z = weatherData["weather"]
                weatherDescription = z[0]["description"]

                temperature.config(text=f"Temperature: {currentTemperature} K")
                windSpeed.config(text=f"Wind Speed: {currentWindSpeed} m/s")
                humidity.config(text=f"Humidity: {currentHumidity} %")
                description.config(text=f"Description: {weatherDescription.capitalize()}")
            except KeyError as e:
                messagebox.showerror("Error", f"Unexpected data format: {e}")
        else:
            messagebox.showerror("Error", "City Not Found. Please check your input.")
    else:
        messagebox.showwarning("Input Error", "Please enter a city name.")



def clear():
    cityEntry.delete(0,tk.END)
    temperature.config(text="Temperature:")
    windSpeed.config(text="Wind Speed:")
    humidity.config(text="Humidity:")
    description.config(text="Description:")
    



# Initialize the main window
root = tk.Tk()
root.geometry("400x300")
root.title("Weather Forecast App")

# Create GUI elements
cityLabel = ttk.Label(root, text="Enter City:")
cityLabel.pack(pady=10)

cityEntry = ttk.Entry(root, width=30)
cityEntry.pack(pady=5)

fetchButton = ttk.Button(root, text="Fetch Weather", command=fetchWeather)
fetchButton.pack(pady=10)

temperature = ttk.Label(root, text="Temperature:")
temperature.pack(pady=5)

humidity = ttk.Label(root, text="Humidity:")
humidity.pack(pady=5)

windSpeed = ttk.Label(root, text="Wind Speed:")
windSpeed.pack(pady=5)

description= ttk.Label(root, text="Description:")
description.pack(pady=5)

clearButton = ttk.Button(root, text="clear", command=clear, width=30)
clearButton.pack(pady=10)





root.mainloop()
