from tkinter import *

def note_taking(root):
    root.title('For Note Taking')

    header = Label(root, text="For Note Taking", font=("Helvetica", 20, "bold"))
    header.grid(row=0, column=0, padx=30, pady=(30, 10))

    global notes_stored

    e_note = Entry(root, width=30, bd=0, bg="light yellow")
    e_note.grid(row=1, column=0)

    #globals()["line_" + str(line)]

def main():
    root = Tk()

    note_taking(root)
    root.mainloop()

if __name__ == "__main__":
    main()
