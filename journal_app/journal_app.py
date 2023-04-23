from tkinter import *
import datetime
import math


def find_month_key():
    match month:
        case 1:
            if year % 4 != 0:
                return 1
            else:
                return 0
        case 2:
            if year % 4 != 0:
                return 4
            else:
                return 3
        case 3:
            return 4
        case 4:
            return 0
        case 5:
            return 2
        case 6:
            return 5
        case 7:
            return 0
        case 8:
            return 3
        case 9:
            return 6
        case 10:
            return 1
        case 11:
            return 4
        case 12:
            return 6


def find_month_name():
    match month:
        case 1:
            return "January"
        case 2:
            return "February"
        case 3:
            return "March"
        case 4:
            return "April"
        case 5:
            return "May"
        case 6:
            return "June"
        case 7:
            return "July"
        case 8:
            return "August"
        case 9:
            return "September"
        case 10:
            return "October"
        case 11:
            return "November"
        case 12:
            return "December"

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

    # check for the calculation bug
    if weekday == 0:
        weekday = ((year + math.floor(year / 4) + current_day + 1 + find_month_key() - 1) % 7)

        # compensates for moving the date by 1
        if weekday != 1:
            weekday -= 1
        else:
            weekday = 7

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
