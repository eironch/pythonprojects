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
    # cursor.execute("""CREATE TABLE addresses (
    #         first_name text,
    #         last_name text,
    #         address text,
    #         city text,
    #         province text,
    #         zipcode integer
    #     )
    # """)

    # Create text boxes
    e_f_name = Entry(root, width=30)
    e_f_name.grid(row=0, column=1, padx=20)
    e_l_name = Entry(root, width=30)
    e_l_name.grid(row=1, column=1, padx=20)
    e_address = Entry(root, width=30)
    e_address.grid(row=2, column=1, padx=20)
    e_city = Entry(root, width=30)
    e_city.grid(row=3, column=1, padx=20)
    e_province = Entry(root, width=30)
    e_province.grid(row=4, column=1, padx=20)
    e_zipcode = Entry(root, width=30)
    e_zipcode.grid(row=5, column=1, padx=20)

    # Create text box labels
    f_name_label = Label(root, text="First Name: ")
    f_name_label.grid(row=0, column=0)
    l_name_label = Label(root, text="Last Name: ")
    l_name_label.grid(row=1, column=0)
    address_label = Label(root, text="Address: ")
    address_label.grid(row=2, column=0)
    city_label = Label(root, text="City: ")
    city_label.grid(row=3, column=0)
    province_label = Label(root, text="Province: ")
    province_label.grid(row=4, column=0)
    zipcode_label = Label(root, text="Zipcode: ")
    zipcode_label.grid(row=5, column=0)

    # Create submit function for database
    def submit():
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')

        # Create cursor
        cursor = conn.cursor()

        # Insert into database table
        cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :province, :zipcode)",
                  {
                      'f_name': e_f_name.get(),
                      'l_name': e_l_name.get(),
                      'address': e_address.get(),
                      'city': e_city.get(),
                      'province': e_province.get(),
                      'zipcode': e_zipcode.get()
                  }
                  )

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

        # Clear text boxes
        e_f_name.delete(0, END)
        e_l_name.delete(0, END)
        e_address.delete(0, END)
        e_city.delete(0, END)
        e_province.delete(0, END)
        e_zipcode.delete(0, END)

    def show_in_window(records):
        # Create new window
        top = Toplevel()
        top.title('Records')

        # Loop through records
        print_records = ''
        for item in range(len(records)):
            for record in records[item]:
                if record == records[item][0]:
                    print_records += f"Record #{item}" + "\n"

                if record != records[item][6]:
                    print_records += str(record) + "\n"
                elif item != len(records) - 1:
                    print (item, len(records) - 1)
                    print_records += "\n"

        query_label = Label(top, text=print_records)
        query_label.grid(row=0, column=0, ipadx=100)

    # Create query function
    def query():
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')

        # Create cursor
        cursor = conn.cursor()

        # Query the database
        cursor.execute("SELECT *, oid FROM addresses")
        records = cursor.fetchall()

        show_in_window(records)

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

    # Create submit button
    submit = Button(root, text="Add Record to Database", width=50, command=submit)
    submit.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Query button
    query = Button(root, text="Show Records", width=50, command=query)
    query.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    mainloop()

if __name__ == "__main__":
    main()