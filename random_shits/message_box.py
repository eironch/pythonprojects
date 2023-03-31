from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def main():
    root = Tk()

    root.title('Messag Boxes')

    # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    def popup():
        if not messagebox.askyesno("Message Box", "Do you like me?"):
            popup()

        else:
            messagebox.showinfo("Message Box", "I like you too!")

    popup()
    quit()
    mainloop()


if __name__ == "__main__":
    main()