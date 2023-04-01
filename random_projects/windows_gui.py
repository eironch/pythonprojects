from tkinter import *
from PIL import ImageTk,Image

def main():
    root = Tk()

    root.title('Window')

    def new_window():
        top = Toplevel()
        top.title('Top Window')
        label = Label(top, text="Good Mourning").pack()

    button = Button(root, text="Open Second Window", command=new_window).pack()

    mainloop()


if __name__ == "__main__":
    main()