from tkinter import *
from PIL import ImageTk,Image

def main():
    root = Tk()

    root.title('Radio Buttons')



    def clicked(value):
        label = Label(root, text=value).pack()

    TOPPINGS = [
        ("Pepperoni", "Pepperoni"),
        ("Cheese","Cheese"),
        ("Mushroom","Mushroom"),
        ("Onion", "Onion")
    ]

    pizza = StringVar()
    pizza.set("Pepperoni")

    for text, topping in TOPPINGS:
        Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)

    button = Button(root, text="Choose!", command=lambda: clicked(pizza.get())).pack()


    mainloop()

if __name__ == "__main__":
    main()