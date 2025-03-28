import db


# db.add_one("Martin", "Gray", "martingray@test.com")

# db.delete_one("2")

# new_customers = [
#     ('Rafael', 'Nadal', 'rafaelnadal@test.com'),
#     ('bob', 'marley', 'bobmarley@test.com')
# ]

# db.add_many(new_customers)

db.show_all()

db.email_lookup("bobmarley@test.com")