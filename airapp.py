from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root= Tk()
root.title("Weather App")
root.iconbitmap("C:/Users/eriol/Desktop/gui_tkinter/ressources/star.ico")
root.geometry("460x100")

#creation de la fonction zipcode
def zipcode():
    # zip.get()
    # zip_label= Label(root, text=zip.get())
    # zip_label.grid(row=1,column=0, columnspan=2)

    try:
        # On crée une variable pour l'API:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=10&API_KEY=3089EE85-FFE1-4338-A885-44B337D77F5D")
        # on crée un nouvelle variable qui va charger le contenu json de l'api 
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality= api[0]['AQI']
        category= api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00" 
        elif category == "Unhalthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000" 
        elif category == "Very Unhealthy":
            weather_color = "#990066" 
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background= weather_color)

        my_label = Label(root, text= city + "/AQ : " + str(quality) + "/" + category, font=("Arial",18),background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)

    except Exception as e:
        api = "ERROR..."

zip = Entry(root)
zip.grid(row=0, column=0,stick= W+E+N+S)
zip_button = Button(root, text="Zipcode", command=zipcode)
zip_button.grid(row=0, column=1,stick= W+E+N+S)

root.mainloop()