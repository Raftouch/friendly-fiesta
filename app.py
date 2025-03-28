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

# c.executemany("INSERT INTO customers (first_name, last_name, email) VALUES (?, ?, ?)", customers)

# c.execute("SELECT * FROM customers")
# c.execute("SELECT rowid, * FROM customers")
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
# c.execute("SELECT * FROM customers WHERE last_name = 'Paris'")
# c.execute("SELECT * FROM customers WHERE last_name LIKE '%an%'")

# c.execute("""UPDATE customers SET first_name = 'Bob'
#           WHERE rowid = 1
#         """)


# fetchOne = c.fetchone()
# print(fetchOne[0])
# print("****************")
# c.fetchmany(3)
items = c.fetchall()
print(items)

for item in items:
    print(item)
    # print(item[0] + " " + item[1] + " \t " + item[2])


connection.commit()

connection.close()

print("Command executed successfully 🙂")
