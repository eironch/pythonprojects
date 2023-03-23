from tkinter import *

def main():
    root = Tk()

    def button_click():
        hello = "Hello " + input.get()
        label1 = Label(root, text=hello)

        label1.pack()

    # creating a label widget and showing it
    label1 = Label(root, text="Good Mourning!")
    label2 = Label(root, text="My name is Cheiron")

    button = Button(root, text="Enter Your Name", padx=50, pady=50, command=button_click)

    input = Entry(root, text="Input Word", width=50)

    label1.pack()
    label2.pack()
    button.pack()
    input.pack()
    input.insert(0, "Insert Your Name: ")

    root.mainloop()



if __name__ == "__main__":
    main()