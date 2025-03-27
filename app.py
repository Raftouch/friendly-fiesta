import sqlite3

# connection = sqlite3.connect(':memory:')
connection = sqlite3.connect('customer.db')

connection = sqlite3.connect('customer.db')

c = connection.cursor()

# c.execute("""CREATE TABLE customers (
#           first_name TEXT,
#           last_name TEXT,
#           email TEXT
#     )""")

# NULL
# INTEGER
# REAL
# TEXT
# BLOB

customers = [
    ('Bob', 'Bryan', 'bobbryan@test.com'),
    ('Alice', 'Paris', 'aliceparis@test.com'),
    ('Anna', 'Banana', 'annabanana@test.com')
]

# c.execute("INSERT INTO customers VALUES ('Bob', 'Bryan', bobbryan@test.com')")

c.executemany("INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)", customers)

connection.commit()

connection.close()

print("Records inserted successfully 🙂")
