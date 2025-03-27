import sqlite3

# connection = sqlite3.connect(':memory:')
connection = sqlite3.connect('customer.db')

connection = sqlite3.connect('customer.db')

c = connection.cursor()

c.execute(""""CREATE TABLE customers (
          first_name TEXT,
          last_name TEXT,
          email TEXT
    )""")

# NULL
# INTEGER
# REAL
# TEXT
# BLOB

c.execute("INSERT INTO customers VALUES ('Bob', 'Bryan', bobbryan@test.com')")

connection.commit()

connection.close()