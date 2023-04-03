from tkinter import *

def main():
    root = Tk()
    root.title('Sliders')
    root.geometry("500x500")

    def slide_update(progress):
        global label
        label.forget()
        label = Label(root, text=progress)
        label.pack()


    def resize():
        root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

    vertical = Scale(root, from_=0, to=1000)
    vertical.set(500)
    vertical.pack()

    horizontal = Scale(root, from_=0, to=1000, orient=HORIZONTAL, command=slide_update)
    horizontal.set(500)
    horizontal.pack()

    button = Button(root, text="resize", command=resize)
    button.pack()

    global label
    label = Label(root, text=horizontal.get())
    label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
