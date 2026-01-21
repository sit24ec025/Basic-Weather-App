import tkinter as tk

# Sample weather data (for demo)
weather_data = {
    "chennai": "Sunny, 34°C",
    "bangalore": "Cloudy, 28°C",
    "delhi": "Hazy, 30°C",
    "mumbai": "Rainy, 29°C",
    "kolkata": "Humid, 32°C"
}

def get_weather():
    city = city_entry.get().lower()

    if city in weather_data:
        result_label.config(text=f"Weather in {city.title()}:\n{weather_data[city]}")
    else:
        result_label.config(text=f"Weather in {city.title()}:\nData not available")

# Main window
root = tk.Tk()
root.title("Simple Weather App")
root.geometry("300x220")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="Simple Weather App", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# City entry
city_entry = tk.Entry(root, font=("Arial", 12), justify="center")
city_entry.pack(pady=5)

# Button
button = tk.Button(root, text="Get Weather", font=("Arial", 11), command=get_weather)
button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.pack(pady=10)

root.mainloop()