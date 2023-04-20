from tkinter import *

def journal(root):
    root.title('Your Journal')
    header = Label(root, text="Your Journal", font=("Helvetica", 20, "bold"))
    header.grid(row=0, column=0, columnspan=10)
def main():
    global root
    root = Tk()

    journal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
