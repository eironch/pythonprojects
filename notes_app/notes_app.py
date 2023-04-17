from tkinter import *
import sqlite3


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

    def enter(*args):
        conn = sqlite3.connect('note_book.db')
        cursor = conn.cursor()

        if root.focus_get() == e_note1:
            get_entry = "e_note1"
            record_id = 1
        elif root.focus_get() == e_note2:
            get_entry = "e_note2"
            record_id = 2
        elif root.focus_get() == e_note3:
            get_entry = "e_note3"
            record_id = 3
        elif root.focus_get() == e_note4:
            get_entry = "e_note4"
            record_id = 4
        else:
            return

        cursor.execute("""UPDATE notebook SET
                          note = :note_submitted

                          WHERE oid = :oid
                          """,
                       {
                           'note_submitted': globals()[get_entry].get(),
                           'oid': record_id
                       }
                       )

        conn.commit()
        conn.close()
        root.focus()

    header = Label(root, text="For Note Taking", font=("Helvetica", 20, "bold"))
    header.grid(row=0, column=0, padx=30, pady=30, columnspan=10)

    for notes in records:
        globals()["note" + str(notes[1])] = Label(root, text="Note " + str(notes[1]) + ": ", font=("Helvetica", 10, "bold"))
        globals()["note" + str(notes[1])].grid(row=notes[1], column=0, padx=(30,0))
        globals()["e_note" + str(notes[1])] = Entry(root, width=30, bd=0, bg="light yellow")
        globals()["e_note" + str(notes[1])].grid(row=notes[1], column=1, padx=(0, 35))
        globals()["e_note" + str(notes[1])].bind('<Return>', enter)
        globals()["e_note" + str(notes[1])].insert(0, (notes[0]))


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
