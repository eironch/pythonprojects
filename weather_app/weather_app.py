from tkinter import *
from PIL import ImageTk,Image
import requests
import json

def main():
    root = Tk()
    root.title('A Weather App')

    # Requests for the api content and show weather
    def show_weather(zip_code):
        try:
            api_requests = requests.get(f"https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zip_code}&date=2023-04-09&distance=5&API_KEY=7F8AC387-7D4E-406A-B367-CBC2BD75C2C2")
            api_content = json.loads(api_requests.content)

            category = api_content[0]['Category']['Name']
            city = api_content[0]['ReportingArea']

            match category:
                case "Good":
                    bg_color = "#00e400"
                case "Moderate":
                    bg_color = "#ffff00"
                case "Unhealthy for Sensitive Groups":
                    bg_color = "#ff7e00"
                case "Unhealthy":
                    bg_color = "#ff0000"
                case "Very Unhealthy":
                    bg_color = "#8f3f97"
                case "Hazardous":
                    bg_color = "#7e0023"

            weather.configure(text=city + " " + category, background=bg_color, font=("Helvetica", 20, "bold"))
            root.configure(background=bg_color)

        except Exception as e:
            api_content = "Error"

    # Removes placeholder text
    def click(*args):
        e_zipcode.delete(0, END)
        e_zipcode.configure(foreground="black")

    def enter(*args):
        show_weather(e_zipcode.get())
        e_zipcode.delete(0, END)
        e_zipcode.insert(0, "Enter zipcode")
        root.focus()

    # Label
    global weather
    weather = Label(root, text="A Weather App", font=("Helvetica", 20, "bold"))
    weather.grid(row=0, column=0, pady=(30,0), padx=30)

    # Entry
    global e_zipcode
    e_zipcode = Entry(root, width=20, foreground="gray")
    e_zipcode.insert(0, "Enter zipcode")
    e_zipcode.grid(row=1, column=0, pady=(30,10))

    # Buttons
    enter_btn = Button(root, text="Get Weather", width=20, borderwidth=3, command=enter)
    enter_btn.grid(row=2, column=0, pady=(0,30))

    # Bindings
    e_zipcode.bind("<Button-1>", click)
    root.bind('<Return>', enter)

    root.mainloop()


if __name__ == "__main__":
    main()