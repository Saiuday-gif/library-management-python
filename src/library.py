from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, membership_id, isbn):
        # Find borrower and book, check availability
        for borrower in self.borrowers:
            if borrower.membership_id == membership_id:
                for book in self.books:
                    if book.isbn == isbn and book.quantity > 0:
                        book.quantity -= 1
                        due_date = datetime.now() + timedelta(days=14)
                        borrower.borrowed_books.append((book, due_date))
                        return True
        return False