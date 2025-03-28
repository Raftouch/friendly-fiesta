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
