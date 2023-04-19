from tkinter import *

def journal(root):
    root.title('Your Journal')

def main():
    global root
    root = Tk()


    journal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
