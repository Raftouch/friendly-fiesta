import sqlite3


def show_all():
    connection = sqlite3.connect('customer.db')
    c = connection.cursor()

    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    connection.commit()
    connection.close()


def add_one(first_name, last_name, email):
    connection = sqlite3.connect('customer.db')
    c = connection.cursor()

    c.execute("INSERT INTO customers VALUES (?,?,?)", (first_name, last_name, email))

    connection.commit()
    connection.close()


def delete_one(id):
    connection = sqlite3.connect('customer.db')
    c = connection.cursor()

    c.execute("DELETE FROM customers WHERE rowid = (?)", id)

    connection.commit()
    connection.close()


def add_many(list):
    connection = sqlite3.connect('customer.db')
    c = connection.cursor()

    c.executemany("INSERT INTO customers VALUES (?,?,?)", list)

    connection.commit()
    connection.close()


def email_lookup(email):
    connection = sqlite3.connect('customer.db')
    c = connection.cursor()

    c.execute("SELECT rowid, * FROM customers WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
        print(item)

    connection.commit()
    connection.close()
