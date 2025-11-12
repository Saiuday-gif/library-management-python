from library import Library
from book import Book
def main():
    library = Library()
    library.add_book(Book("The Catcher in the Rye", "6789345567333", "J.D. Salinger", 1)) 
    library.add_book(Book("1984", "6789345567333", "George Orwell", 2))

    while True:
        print("\n#UPDATED:- Library Management System")
        print("1. Add Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display All Books")
        print("5. Exit")
        choice = input("\nEnter choice: ")
        if choice == '5':
            print("Exiting the system. Goodbye!")
            break
        elif choice == '1':
            print("\nAdd New Book")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            genre = input("Enter book genre: ")
            try:
             quantity_str = int(input("Enter quantity: "))
             quantity = int(quantity_str)
            except ValueError:
             print("ERROR:Invalid quantity. Setting quantity to 1.")
             quantity = 1
            library.add_book(Book(title, author, isbn, genre, quantity))
            print(f"Book '{title}' added successfully.")
        elif choice == '2':
            print("\nBorrow Book")
            membership_id = input("Enter membership ID: ")
            isbn = input("Enter book ISBN to borrow: ")
            if library.borrow_book(membership_id, isbn):
                print("Book borrowed successfully.")
            else:
                print("Failed to borrow book. Check membership ID or book availability.")
        elif choice == '3':
            print("\nReturn Book")
            membership_id = input("Enter membership ID: ")
            isbn = input("Enter book ISBN to return: ")
            if library.return_book(membership_id, isbn):
                print("Book returned successfully.")
            else:
                print("Failed to return book. Check membership ID or ISBN.")
        elif choice == '4':
            print("\nAll Books in Library:")
            library.display_books()
        else:
            print("Invalid choice. Please try again.")
        # Handle other choices...q

if __name__ == "__main__":
    main()