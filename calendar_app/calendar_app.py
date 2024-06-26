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


def find_days_in_month():
    match month:
        case 1:
            return 31
        case 2:
            if year % 4 != 0:
                return 28
            else:
                return 29
        case 3:
            return 31
        case 4:
            return 30
        case 5:
            return 31
        case 6:
            return 30
        case 7:
            return 31
        case 8:
            return 31
        case 9:
            return 30
        case 10:
            return 31
        case 11:
            return 30
        case 12:
            return 31


def previous_month():
    global month
    global year

    destroy_calendar()

    if month != 1:
        month -= 1
    else:
        year -= 1
        month = 12

    create_calendar()


def next_month():
    global month
    global year

    destroy_calendar()

    if month != 12:
        month += 1
    else:
        year += 1
        month = 1

    create_calendar()


def destroy_calendar():
    week = 0
    weekday = ((year + math.floor(year / 4) + 2 + find_month_key() - 1) % 7)

    # compensates for starting in day 2
    if weekday != 1:
        weekday -= 1
    else:
        weekday = 7

    # makes value start from base 0
    if weekday != 0:
        weekday -= 1
    else:
        weekday = 6

    for days in range(1, find_days_in_month() + 1):
        globals()["day_" + str(days)].destroy()

        weekday += 1

        if weekday % 7 == 0:
            week += 1
            weekday = 0


def create_calendar():
    week = 0
    weekday = ((year + math.floor(year / 4) + 2 + find_month_key() - 1) % 7)

    # compensates for starting in day 2
    if weekday != 0:
        weekday -= 1
    else:
        weekday = 6

    # makes value start from base 0
    if weekday != 0:
        weekday -= 1
    else:
        weekday = 6

    for day in range(1, find_days_in_month() + 1):
        globals()["day_" + str(day)] = Label(root, text=day, width=10, height=5)
        globals()["day_" + str(day)].grid(row=week + 3, column=weekday)

        if current_day == day and current_month == month and current_year == year :
            globals()["day_" + str(day)].configure(bg="light gray")

        weekday += 1

        if weekday % 7 == 0:
            week += 1
            weekday = 0

    month_name = find_month_name()
    month_label.configure(text=month_name, font=("Helvetica", 20))
    year_label2.configure(text=year, font=("Helvetica", 20))


def main():
    global root
    root = Tk()
    root.title('Just a Calendar')

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

    # app title label
    header = Label(root, text="Just a Calendar", font=("Helvetica", 20, "bold"))
    header.grid(row=0, column=0, columnspan=7, padx=30, pady=(30, 10))

    # month name label
    global month_label
    month_label = Label(root)
    month_label.grid(row=1, column=0, columnspan=7, padx=30, pady=30)

    # current year labels
    year_label1 = Label(root, text="20", font=("Helvetica", 20))
    year_label1.grid(row=1, column=0)
    global year_label2
    year_label2 = Label(root)
    year_label2.grid(row=1, column=6)

    # weekday labels
    weekday_label_row = 2
    global label_width
    label_width = 10
    sunday_label = Label(root, text="Sunday", width=label_width)
    sunday_label.grid(row=weekday_label_row, column=0)
    monday_label = Label(root, text="Monday", width=label_width)
    monday_label.grid(row=weekday_label_row, column=1)
    tuesday_label = Label(root, text="Tuesday", width=label_width)
    tuesday_label.grid(row=weekday_label_row, column=2)
    wednesday_label = Label(root, text="Wednesday", width=label_width)
    wednesday_label.grid(row=weekday_label_row, column=3)
    thursday_label = Label(root, text="Thursday", width=label_width)
    thursday_label.grid(row=weekday_label_row, column=4)
    friday_label = Label(root, text="Friday", width=label_width)
    friday_label.grid(row=weekday_label_row, column=5)
    saturday_label = Label(root, text="Saturday", width=label_width)
    saturday_label.grid(row=weekday_label_row, column=6)

    # control buttons
    button_previous = Button(root, text="<", width=2, height=1, command=previous_month)
    button_previous.grid(row=1, column=1)
    button_next = Button(root, text=">", width=2, height=1, command=next_month)
    button_next.grid(row=1, column=5)

    create_calendar()
    root.mainloop()


if __name__ == "__main__":
    main()
