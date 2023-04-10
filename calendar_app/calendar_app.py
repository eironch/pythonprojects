from tkinter import *
from tkcalendar import Calendar
from PIL import ImageTk,Image
import math

def main():
    root = Tk()
    root.title('Just a Calendar')
    week = 0
    weekday = 0
    weekday_label_width = 10

    header = Label(root, text="Just a Calendar", font=("Helvetica", 20, "bold"))
    header.grid(row=0, column=0, columnspan=7, padx= 30, pady=(30,10))

    month_label = Label(root, text="April", font=("Helvetica", 20))
    month_label.grid(row=1, column=0, columnspan=7, padx= 30, pady=30)

    weekday_label_row = 2
    sunday_label = Label(root, text="Sunday", width=weekday_label_width)
    sunday_label.grid(row=weekday_label_row, column=0)
    monday_label = Label(root, text="Monday", width=weekday_label_width)
    monday_label.grid(row=weekday_label_row, column=1)
    tuesday_label = Label(root, text="Tueday", width=weekday_label_width)
    tuesday_label.grid(row=weekday_label_row, column=2)
    wednesday_label = Label(root, text="Wednesday", width=weekday_label_width)
    wednesday_label.grid(row=weekday_label_row, column=3)
    thursday_label = Label(root, text="Thursday", width=weekday_label_width)
    thursday_label.grid(row=weekday_label_row, column=4)
    friday_label = Label(root, text="Friday", width=weekday_label_width)
    friday_label.grid(row=weekday_label_row, column=5)
    saturday_label = Label(root, text="Saturday", width=weekday_label_width)
    saturday_label.grid(row=weekday_label_row, column=6)

    def find_month_key(month):
        match month:
            case 1:
                return 1
            case 2:
                return 4
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
    year = 23
    month = 1

    weekday = ((year + math.floor(year/4) + 2 + find_month_key(month) - 1) % 7) - 1

    if weekday != 0:
        weekday -= 1
    else:
        weekday = 6

    for days in range(1, 32):

        Label(root, text=days).grid(row=week+3, column=weekday, pady=30)
        weekday += 1

        if weekday % 7 == 0:
            week += 1
            weekday = 0

    root.mainloop()


if __name__ == "__main__":
    main()