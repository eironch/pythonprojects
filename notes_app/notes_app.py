from tkinter import *
import sqlite3
from PIL import ImageTk,Image

def create_table(cursor):
    try:
        conn = sqlite3.connect('note_book.db')
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE notebook (
                note text
            )
        """)
        for x in range(4):
            cursor.execute("INSERT INTO notebook VALUES (:note)",
                           {
                               'note' : ""
                           }
                           )

        conn.commit()
        conn.close()
    except:
        return


def query_table(cursor):
    cursor.execute("SELECT *, oid FROM notebook")
    records = cursor.fetchall()
    return records


def note_taking(root, records):
    root.title('For Note Taking')
    #root.geometry("331x274")

    global status
    status = "Saved"

    def save_notes(*args):
        global status
        global img_status

        if status == "Not Saved":
            status = "Saved"
            img_status.configure(image=root.green_circle)

        conn = sqlite3.connect('note_book.db')
        cursor = conn.cursor()

        for x in range(1,5):
            cursor.execute("""UPDATE notebook SET
                              note = :note_submitted
    
                              WHERE oid = :oid
                              """,
                           {
                               'note_submitted': globals()["e_note" + str(x)].get(),
                               'oid': x
                           }
                           )

        conn.commit()
        conn.close()
        root.focus()

    def update_status(*args):
        global status
        global img_status

        if status == "Saved":
            status = "Not Saved"
            img_status.configure(image=root.red_circle)

    header = Label(root, text="For Note Taking", font=("Helvetica", 20, "bold"))
    header.grid(row=0, column=0, padx=30, pady=30, columnspan=10)

    for notes in records:
        globals()["note" + str(notes[1])] = Label(root, text="Note " + str(notes[1]) + ": ", font=("Helvetica", 10, "bold"))
        globals()["note" + str(notes[1])].grid(row=notes[1], column=0, padx=(30,0))
        globals()["e_note" + str(notes[1])] = Entry(root, width=30, bd=0, bg="light yellow", insertwidth=1, font=("Helvetica", 10))
        globals()["e_note" + str(notes[1])].grid(row=notes[1], column=1, padx=(0, 35))
        globals()["e_note" + str(notes[1])].bind('<Return>', save_notes)
        globals()["e_note" + str(notes[1])].bind('<Any-KeyPress>', update_status)
        globals()["e_note" + str(notes[1])].insert(0, (notes[0]))

    btn_save = Button(root, text="Save Notes", width=30, height=2, font=("Helvetica", 10), command=save_notes)
    btn_save.grid(row=5, column=0, columnspan=2, pady=30)

    root.green_circle = ImageTk.PhotoImage(Image.open("images/green.png").resize((10, 10), Image.LANCZOS))
    root.red_circle = ImageTk.PhotoImage(Image.open("images/red.png").resize((10, 10), Image.LANCZOS))

    global img_status
    img_status = Label(root, image=root.green_circle)
    img_status.grid(row=5, column=0, columnspan=2, rowspan=10, padx=(225,0), pady=(0,20))


def main():
    root = Tk()

    conn = sqlite3.connect('note_book.db')
    cursor = conn.cursor()


    create_table(cursor)
    note_taking(root, query_table(cursor))

    conn.commit()
    conn.close()

    root.mainloop()


if __name__ == "__main__":
    main()
