from tkinter import *


def main():
    global root
    root = Tk()
    root.title('For Note Taking')

    e_note = Entry(root, width=30, bd=0)
    e_note.grid()

    root.mainloop()

if __name__ == "__main__":
    main()
