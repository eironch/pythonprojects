from tkinter import *
import sqlite3

def create_table(cursor):
    try:
        cursor.execute("""CREATE TABLE notebook (
                notes text
            )
        """)
    except:
        return
def query_table(cursor):
    return

def note_taking(root, records):
    root.title('For Note Taking')

    def enter(*args):
        conn = sqlite3.connect('note_book.db')
        cursor = conn.cursor()

        if root.focus_get() == e_note1:
            get_entry = "e_note1"
            record_id = 0
        elif root.focus_get() == e_note2:
            get_entry = "e_note2"
            record_id = 1
        elif root.focus_get() == e_note3:
            get_entry = "e_note3"
            record_id = 2
        elif root.focus_get() == e_note4:
            get_entry = "e_note4"
            record_id = 3
        else:
            return

        # just check if it contains anything then do update if not
        cursor.execute("""INSERT INTO notebook (notes) VALUES(:note_submitted)
  ON                      CONFLICT(notes) DO UPDATE SET phonenumber=:note_submitted""",
                       {
                           'note_submitted': globals()[get_entry].get()
                       }
                       )

        cursor.execute("SELECT *, oid FROM notebook")
        records = cursor.fetchall()
        print(records)
        return records

        conn.commit()
        conn.close()
        root.focus()

    header = Label(root, text="For Note Taking", font=("Helvetica", 20, "bold"))
    header.grid(row=0, column=0, padx=30, pady=30, columnspan=10)

    for x in range(1,5):
        globals()["note" + str(x)] = Label(root, text="Note " + str(x) + ": ", font=("Helvetica", 10, "bold"))
        globals()["note" + str(x)].grid(row=x, column=0, padx=(30,0))
        globals()["e_note" + str(x)] = Entry(root, width=30, bd=0, bg="light yellow")
        globals()["e_note" + str(x)].grid(row=x, column=1, padx=(0, 35))
        globals()["e_note" + str(x)].bind('<Return>', enter)

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
