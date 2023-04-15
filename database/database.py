from tkinter import *
from PIL import ImageTk,Image
import sqlite3

def create_table(cursor):
    try:
        cursor.execute("""CREATE TABLE addresses (
                first_name text,
                last_name text,
                address text,
                city text,
                province text,
                zipcode integer
            )
        """)

    except:
        return

def database(root):
    # Create text boxes
    e_f_name = Entry(root, width=30)
    e_f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
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
    e_select = Entry(root, width=30)
    e_select.grid(row=8, column=1, padx=20)

    # Create text box labels
    f_name_label = Label(root, text="First Name: ")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
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
    select_label = Label(root, text="Record ID: ")
    select_label.grid(row=8, column=0)

    # Create function to delete record
    def delete():
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        # Create cursor
        cursor = conn.cursor()

        # Delete a record
        cursor.execute("DELETE from addresses WHERE oid= " + e_delete.get())

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

    # Create submit function for database
    def submit():
        if len(e_f_name.get()) == 0:
            return

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

    # Shows records in new window
    def show_in_window(records):
        # Create new window
        top = Toplevel()
        top.title('Records')

        # Loop through records
        print_records = ''
        for item in range(len(records)):
            for record in records[item]:
                if record == records[item][0]:
                    print_records += f"Record #{records[item][6]}" + "\n"

                if record != records[item][6]:
                    print_records += str(record) + "\n"
                elif item != len(records) - 1:
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

    # Create update data in database
    def update():
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')

        # Create cursor
        cursor = conn.cursor()
        cursor.execute("""UPDATE addresses SET
                   first_name = :f_name,
                   last_name = :l_name,
                   address = :address,
                   city = :city,
                   province = :province,
                   zipcode = :zipcode

                   WHERE oid = :oid
                   """,
                       {
                           'f_name': e_f_name_editor.get(),
                           'l_name': e_l_name_editor.get(),
                           'address': e_address_editor.get(),
                           'city': e_city_editor.get(),
                           'province': e_province_editor.get(),
                           'zipcode': e_zipcode_editor.get(),
                           'oid': record_id
                       }
                       )

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

        # Clear text boxes
        e_f_name_editor.delete(0, END)
        e_l_name_editor.delete(0, END)
        e_address_editor.delete(0, END)
        e_city_editor.delete(0, END)
        e_province_editor.delete(0, END)
        e_zipcode_editor.delete(0, END)

        top.destroy()

    # Show selected record in a new window to be updated
    def edit(id):
        global top
        top = Toplevel()
        top.title('Update Record')

        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')

        # Create cursor
        cursor = conn.cursor()

        # Query the database
        global record_id
        record_id = id
        cursor.execute("SELECT * FROM addresses WHERE oid= " + record_id)
        records = cursor.fetchall()

        global e_f_name_editor
        global e_l_name_editor
        global e_address_editor
        global e_city_editor
        global e_province_editor
        global e_zipcode_editor

        # Create text boxes
        e_f_name_editor = Entry(top, width=30)
        e_f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        e_l_name_editor = Entry(top, width=30)
        e_l_name_editor.grid(row=1, column=1, padx=20)
        e_address_editor = Entry(top, width=30)
        e_address_editor.grid(row=2, column=1, padx=20)
        e_city_editor = Entry(top, width=30)
        e_city_editor.grid(row=3, column=1, padx=20)
        e_province_editor = Entry(top, width=30)
        e_province_editor.grid(row=4, column=1, padx=20)
        e_zipcode_editor = Entry(top, width=30)
        e_zipcode_editor.grid(row=5, column=1, padx=20)

        # Create text box labels
        f_name_label = Label(top, text="First Name: ")
        f_name_label.grid(row=0, column=0, pady=(10, 0))
        l_name_label = Label(top, text="Last Name: ")
        l_name_label.grid(row=1, column=0)
        address_label = Label(top, text="Address: ")
        address_label.grid(row=2, column=0)
        city_label = Label(top, text="City: ")
        city_label.grid(row=3, column=0)
        province_label = Label(top, text="Province: ")
        province_label.grid(row=4, column=0)
        zipcode_label = Label(top, text="Zipcode: ")
        zipcode_label.grid(row=5, column=0)

        update_btn = Button(top, text="Update Record", width=50, command=update)
        update_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        # Loop through results
        for record in records:
            e_f_name_editor.insert(0, record[0])
            e_l_name_editor.insert(0, record[1])
            e_address_editor.insert(0, record[2])
            e_city_editor.insert(0, record[3])
            e_province_editor.insert(0, record[4])
            e_zipcode_editor.insert(0, record[5])

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

    # Create submit button
    submit_btn = Button(root, text="Add Record to Database", width=50, command=submit)
    submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Query button
    query_btn = Button(root, text="Show Records", width=50, command=query)
    query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    # Create a update button
    edit_btn = Button(root, text="Edit Record", width=50, command=lambda: edit(e_select.get()))
    edit_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

    # Create a delete button

    delete_btn = Button(root, text="Delete Record", width=50, command=delete)
    delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

def main():
    root = Tk()

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    cursor = conn.cursor()

    create_table(cursor)
    database(root)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()

    mainloop()

if __name__ == "__main__":
    main()