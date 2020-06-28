import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return connection

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def table_main():

    database = "contacts.db"
    conn = create_connection(database)
    sql_create_contacts_table = ''' CREATE TABLE IF NOT EXISTS phonebook (
                                        id integer PRIMARY KEY,
                                        first_name text NOT NULL,
                                        last_name  text,
                                        phone_number text
                                    );'''

    with conn:
        create_table(conn, sql_create_contacts_table)

def create_contact(conn, new_contact):
    sql = '''INSERT INTO phonebook(first_name, last_name, phone_number)
            values(?,?,?)'''
    c= conn.cursor()
    c.execute(sql,new_contact)

def insert_main():
    database = "contacts.db"
    conn = create_connection(database)

    with conn:
        new_contact=(first_name, last_name, phone_number)
        create_contact(conn, new_contact)

def find_contact(conn, old_contact):
    c = conn.cursor()
    #sql = 'SELECT * FROM phonebook where first_name like ?'
    c.execute("SELECT * FROM phonebook where first_name like '%{}%'".format (old_contact))

    rows = c.fetchall()

    for row in rows:
        print(row)

def select_main():
    database = "contacts.db"

    conn = create_connection(database)

    with conn:
        print('Find Contact')
        find_contact(conn, old_name)

def modify_contact(conn, modified_contact):

    if mod_contact == 'First Name':
        sql = '''UPDATE phonebook 
                set first_name = ?
                where id = ?
                '''
    elif mod_contact == 'Last Name':
        sql = '''UPDATE phonebook
                set last_name = ?
                where id = ?
                 '''
    elif mod_contact == 'Phone Number':
        sql = '''UPDATE phonebook
               set phone_number = ?
               where id = ? 
              '''
    else:
        sql = ''' UPDATE phonebook
              set first_name = ?
              last_name = ?
              phone_number = ?
              where id = ?
              '''
    c = conn.cursor()
    c.execute(sql, modified_contact)
    conn.commit()
    print("Contact Updated successfully")

def update_main():
    database = "contacts.db"
    conn = create_connection(database)

    with conn:
        if mod_contact == 'First Name':
            modify_contact(conn,(new_first_name, id))
        elif mod_contact == 'Last Name':
            modify_contact(conn,(new_last_name, id))
        elif mod_contact == 'Phone Number':
            modify_contact(conn,(new_number, id))
        else:
            modify_contact(conn,(new_first_name, new_last_name, new_number, id))

def delete_contact(conn, delete_id):

    sql = 'DELETE FROM phonebook where id = ?'
    c = conn.cursor()
    c.execute(sql, (id,))
    conn.commit()
    print("Deleted!")

def delete_main():
    database = "contacts.db"
    conn = create_connection(database)

    with conn:
        delete_contact(conn, id)

if __name__ == "__main__":
    table_main() 

print('Welcome to your phonebook, please input create/find in the textbox below')
action= input('Please input action here: ' )

if action == 'create':
    first_name=input('Kindly provide first name: ')
    last_name = input('kindly provide last name: ')
    phone_number = input('kindly provide phone number: ')

    insert_main()

    print('New contact created')

elif action == 'find':

    old_name = input('Kindly provide contact first name: ')

    select_main()

    print("Do you wish to update/delete this contact?, please input update/delete in the textbox below")

    update_delete = input('kindly indicate your preference: ')

    if update_delete == 'update':

        mod_contact = input('What detail do you want to edit: First Name, Last Name, Phone Number, All?: ')

        if mod_contact == 'First Name': 
            new_first_name = input('kindly provide the new first name: ')

        elif mod_contact == 'Last Name':
            new_last_name = input('kindly provide the new last name: ')

        elif mod_contact == 'Phone Number':
            new_number = input('kindly provide the new number: ')

        else:
            new_first_name = input('kindly provide the new first name: ')
            new_last_name = input('kindly provide the new last name: ')
            new_number = input('kindly provide the new number: ')
            id = input('kindly input the corresponding id of the contact: ')

        id = input('kindly input the corresponding id of the contact: ')
        
        update_main()

    elif update_delete == 'delete':
        id = input('kindly input the corresponding id of the contact: ')
        delete_main()

