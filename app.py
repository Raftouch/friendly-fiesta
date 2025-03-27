import sqlite3

# connection = sqlite3.connect(':memory:')
connection = sqlite3.connect('customer.db')

connection = sqlite3.connect('customer.db')

c = connection.cursor()

c.execute(""""CREATE TABLE cutomers (
          first_name TEXT,
          last_name TEXT,
          email TEXT
    )""")

# NULL
# INTEGER
# REAL
# TEXT
# BLOB

connection.commit()

connection.close()