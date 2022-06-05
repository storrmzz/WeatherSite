import tkinter as tk
import requests

def getWeather():
    api = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset&current_weather=true&timezone=Europe%2FBerlin"
    json_data = requests.get(api).json()
    temp_min = str(json_data["daily"]["temperature_2m_min"][0])
    temp_max = str(json_data["daily"]["temperature_2m_max"][0])
    sunrise = str(json_data["daily"]["sunrise"][0])
    sunset = str(json_data["daily"]["sunset"][0])
    temp_now = str(json_data["current_weather"]["temperature"])
    wind = str(json_data["current_weather"]["windspeed"])
    time = str(json_data["current_weather"]["time"])

    final_temp_min_day = "Mind. Temperatur: " + str(temp_min) + " ℃"
    label1.config(text = final_temp_min_day)

    final_temp_max_day = "Max. Temperatur: " + str(temp_max) + " ℃"
    label4.config(text = final_temp_max_day)

    final_sunrise_day = "Sonnenaufgang: " + str(sunrise)[11:16] + " Uhr"
    label5.config(text = final_sunrise_day)

    final_sunset_day = "Sonnenuntergang: " + str(sunset)[11:16] + " Uhr"
    label6.config(text = final_sunset_day)

    final_temp_now = "Temperatur: " + str(temp_now) + " ℃"
    label2.config(text = final_temp_now)

    final_wind_now = "Windgeschwindigkeit: " + str(wind) + " km/h"
    label3.config(text = final_wind_now)

    final_time_now = "Uhrzeit: " + str(time)[11:16] + " Uhr"
    label7.config(text = final_time_now)

canvas = tk.Tk()
canvas.geometry("900x600")
canvas.title("Wetter-App")

f = ("poppins", 15, "bold",)
t = ("poppins", 35, "bold")

dayFrame = tk.Frame(canvas)
nowFrame = tk.Frame(canvas)

title = tk.Label(canvas, font = t)
title.config(text="Wetter-App", underline=True, fg="blue")
title.pack(padx= 1, pady=1)

title2 = tk.Label(canvas, font = ("Courier", 16, "italic"))
title2.config(text="Heute:", underline=True, fg="blue")
title2.pack(padx=10, pady=50)
title2.place(x=250,y=100)

title3 = tk.Label(canvas, font = ("Courier", 16, "italic"))
title3.config(text="Jetzt:", underline=True, fg="blue")
title3.pack(padx=10, pady=50)
title3.place(x=250,y=360)

label1 = tk.Label(dayFrame, font = f)
label1.pack()

label2 = tk.Label(nowFrame, font = f)
label2.pack()

label3 = tk.Label(nowFrame, font = f)
label3.pack()

label4 = tk.Label(dayFrame, font = f)
label4.pack()

label5 = tk.Label(dayFrame, font = f)
label5.pack()

label6 = tk.Label(dayFrame, font = f)
label6.pack()

label7 = tk.Label(nowFrame, font = f)
label7.pack()

dayFrame.pack(padx=80, pady=80)
nowFrame.pack(padx=90, pady=50)

getWeather()

canvas.mainloop()