from tkinter import *
from PIL import ImageTk,Image
import sqlite3

def main():
    root = Tk()
    root.title('Database')

    # Create a database or connect to one

    conn = sqlite3.connect('address_book.db')

    # Create cursor
    cursor = conn.cursor()

    # Create table
    cursor.execute("""CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            province text,
            zipcode integer
        )
    """)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    mainloop()

if __name__ == "__main__":
    main()