from tkinter import *
import datetime
import math

def journal(root):
    root.title('Your Journal')

    global year
    global month
    global current_date
    global current_day
    global current_month
    global current_year
    current_date = datetime.datetime.now()
    current_day = int(current_date.strftime("%d"))
    current_month = int(current_date.strftime("%m"))
    current_year = int(current_date.strftime("%y"))
    year = int(current_date.strftime("%y"))
    month = int(current_date.strftime("%m"))

    weekday = ((year + math.floor(year / 4) + current_day + find_month_key() - 1) % 7)
    print(weekday)
    header = Label(root, text="Your Journal", font=("Helvetica", 20, "bold"))
    header.grid(row=0, column=0, columnspan=10, padx=30, pady=(30,10))

    weekday_list = ["Sunday",
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday"
                    ]

    for x in range(7):
        globals()["weekday_" + str(x + 1)] = Label(root, text=weekday_list[x], font=("Helvetica", 10))
        globals()["weekday_" + str(x + 1)].grid(row = 1, column = x, padx=30)


def main():
    global root
    root = Tk()

    journal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
