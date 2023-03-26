from tkinter import *
from PIL import ImageTk,Image
import re

def main():
    root = Tk()

    # variables
    button_width = 10
    button_height = 3
    button_grid_padx = 2
    button_grid_pady = 2

    # images
    root.iconbitmap('calculator.ico')
    img = ImageTk.PhotoImage(Image.open('calculator.png').resize((50, 50), Image.LANCZOS))

    # texts
    root.title("The Calculator")

    e = Entry(root, width=45, borderwidth=5, justify="right")
    e.insert(0, 0)

    # functions
    def button_click(num):
        if e.get() == "0":
            e.delete(0, END)

        e.insert(END, num)

    def button_clear():
        e.delete(0, END)
        e.insert(0, 0)

    def button_all_clear():
        global f_num
        f_num = 0

        e.delete(0, END)
        e.insert(0, 0)

    def button_add():
        global operation
        operation = "addition"

        global f_num
        first_number = e.get()
        f_num = int(float(first_number))

        e.delete(0, END)
        e.insert(0, 0)

    def button_subtract():
        global operation
        operation = "subtraction"

        global f_num
        first_number = e.get()
        f_num = int(float(first_number))

        e.delete(0, END)
        e.insert(0, 0)

    def button_multiply():
        global operation
        operation = "multiply"

        global f_num
        first_number = e.get()
        f_num = int(float(first_number))

        e.delete(0, END)
        e.insert(0, 0)

    def button_divide():
        global operation
        operation = "division"

        global f_num
        first_number = e.get()
        f_num = int(float(first_number))

        e.delete(0, END)
        e.insert(0, 0)

    def button_equal():
        second_number = float(e.get())

        if operation == "addition":
            result = second_number + f_num
        elif operation == "subtraction":
            result = second_number - f_num
        elif operation == "multiply":
            result = second_number * f_num
        elif operation == "division":
            result = f_num / second_number
        else:
            return

        if result.is_integer():
            result = int(result)

        e.delete(0, END)
        e.insert(0, result)

    # buttons
    button_1 = Button(root, text="1", width=button_width, height=button_height, command=lambda: button_click(1))
    button_2 = Button(root, text="2", width=button_width, height=button_height, command=lambda: button_click(2))
    button_3 = Button(root, text="3", width=button_width, height=button_height, command=lambda: button_click(3))
    button_4 = Button(root, text="4", width=button_width, height=button_height, command=lambda: button_click(4))
    button_5 = Button(root, text="5", width=button_width, height=button_height, command=lambda: button_click(5))
    button_6 = Button(root, text="6", width=button_width, height=button_height, command=lambda: button_click(6))
    button_7 = Button(root, text="7", width=button_width, height=button_height, command=lambda: button_click(7))
    button_8 = Button(root, text="8", width=button_width, height=button_height, command=lambda: button_click(8))
    button_9 = Button(root, text="9", width=button_width, height=button_height, command=lambda: button_click(9))
    button_0 = Button(root, text="0", width=button_width, height=button_height, command=lambda: button_click(0))

    button_clear = Button(root, text="C", width=button_width * 2 + 2, height=button_height, command=button_clear)
    button_all_clear = Button(root, text="AC", width=button_width * 2 + 2, height=button_height, command=button_all_clear)

    button_add = Button(root, text="+", width=button_width, height=button_height, command=button_add)
    button_subtract = Button(root, text="-", width=button_width, height=button_height, command=button_subtract)
    button_multiply = Button(root, text="*", width=button_width, height=button_height, command=button_multiply)
    button_divide = Button(root, text="/", width=button_width, height=button_height, command=button_divide)

    button_equal = Button(root, text="=", width=button_width * 4 + 6, height=button_height, command=button_equal)

    button_quit = Button(root, text="Quit", activebackground="light gray", relief="flat", overrelief="solid", bd=0, width=5, height=1, command=root.quit)

    # draw
    e.grid(row=1, column=0, columnspan=4, padx = 10, pady = 10)

    button_1.grid(row=5, column=0, padx=button_grid_padx, pady=button_grid_pady)
    button_2.grid(row=5, column=1, padx=button_grid_padx, pady=button_grid_pady)
    button_3.grid(row=5, column=2, padx=button_grid_padx, pady=button_grid_pady)

    button_4.grid(row=4, column=0, padx=button_grid_padx, pady=button_grid_pady)
    button_5.grid(row=4, column=1, padx=button_grid_padx, pady=button_grid_pady)
    button_6.grid(row=4, column=2, padx=button_grid_padx, pady=button_grid_pady)

    button_7.grid(row=3, column=0, padx=button_grid_padx, pady=button_grid_pady)
    button_8.grid(row=3, column=1, padx=button_grid_padx, pady=button_grid_pady)
    button_9.grid(row=3, column=2, padx=button_grid_padx, pady=button_grid_pady)

    button_0.grid(row=6, column=1, padx=button_grid_padx, pady=button_grid_pady)

    button_clear.grid(row=2, column=2, columnspan=2, padx=button_grid_padx, pady=button_grid_pady)
    button_all_clear.grid(row=2, column=0, columnspan=2, padx=button_grid_padx, pady=button_grid_pady)

    button_divide.grid(row=3, column=3, padx=button_grid_padx, pady=button_grid_pady)
    button_multiply.grid(row=4, column=3, padx=button_grid_padx, pady=button_grid_pady)
    button_subtract.grid(row=5, column=3, padx=button_grid_padx, pady=button_grid_pady)
    button_add.grid(row=6, column=3, padx=button_grid_padx, pady=button_grid_pady)

    button_equal.grid(row=7, column=0, columnspan=4, padx=button_grid_padx, pady=button_grid_pady)

    button_quit.grid(row=0, column=0, padx=button_grid_padx, pady=button_grid_pady)

    root.mainloop()

if __name__ == "__main__":
    main()
