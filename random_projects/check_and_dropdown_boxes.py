from tkinter import *

def main():
    root = Tk()
    root.title('Sliders')
    root.geometry("500x500")

    def show_selected_check():
        label = Label(root, text=var.get() + " " + clicked.get())
        label.pack()
    def show_selected_drop(day):
        label = Label(root, text=var.get() + " " + day)
        label.pack()

    var = StringVar()
    c = Checkbutton(root, text="Switch", variable=var, command=show_selected_check, onvalue="on", offvalue="off")
    c.deselect()
    c.pack()

    options = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
    clicked = StringVar()
    clicked.set(options[0])
    drop = OptionMenu(root, clicked, *options, command=show_selected_drop)
    drop.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
