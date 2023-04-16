from tkinter import *

def note_taking(root):
    root.title('For Note Taking')

    def enter(*args):
        print("yes")
        root.focus()

    header = Label(root, text="For Note Taking", font=("Helvetica", 20, "bold"))
    header.grid(row=0, column=0, padx=30, pady=(30, 10), columnspan=10)

    for x in range(1,5):
        globals()["note" + str(x)] = Label(root, text="Note " + str(x) + ": ", font=("Helvetica", 10, "bold"))
        globals()["note" + str(x)].grid(row=x, column=0, padx=(30,0))
        globals()["e_note" + str(x)] = Entry(root, width=30, bd=0, bg="light yellow")
        globals()["e_note" + str(x)].grid(row=x, column=1, padx=(0, 35))
        globals()["e_note" + str(x)].bind('<Return>', enter)

def main():
    root = Tk()

    note_taking(root)
    root.mainloop()

if __name__ == "__main__":
    main()
