class Book:
    def __init__(self, title, author, isbn, genre="General", quantity=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity
        self.available = True 
    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Quantity cannot be negative.")