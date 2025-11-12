class Borrower:
    def __init__(self, name, contact, membership_id):
        self.name = name
        self.contact = contact
        self.membership_id = membership_id
        self.borrowed_books = []  # List to track borrowed books

    def update_contact(self, new_contact):
        self.contact = new_contact