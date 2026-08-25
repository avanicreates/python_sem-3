class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_book(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ID: {self.book_id} | Title: {self.title} | "
              f"Author: {self.author} | Status: {status}")


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display_patron(self):
        print(f"ID: {self.patron_id} | Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:", ", ".join(self.borrowed_books))
        else:
            print("Borrowed Books: None")


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists.")
        else:
            self.books[book.book_id] = book
            print("Book added successfully.")

    def register_patron(self, patron):
        if patron.patron_id in self.patrons:
            print("Patron ID already exists.")
        else:
            self.patrons[patron.patron_id] = patron
            print("Patron registered successfully.")

    def borrow_book(self, book_id, patron_id):
        if book_id not in self.books:
            print("Book not found.")
            return

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print("Book is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book.title)
            print(f"'{book.title}' borrowed successfully by {patron.name}.")

    def return_book(self, book_id, patron_id):
        if book_id not in self.books:
            print("Book not found.")
            return

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if not book.is_borrowed:
            print("This book is not currently borrowed.")
        elif book.title not in patron.borrowed_books:
            print("This patron did not borrow this book.")
        else:
            book.is_borrowed = False
            patron.borrowed_books.remove(book.title)
            print(f"'{book.title}' returned successfully.")

    def display_books(self):
        print("\n--- Library Books ---")
        if not self.books:
            print("No books available.")
        else:
            for book in self.books.values():
                book.display_book()

    def display_patrons(self):
        print("\n--- Library Patrons ---")
        if not self.patrons:
            print("No patrons registered.")
        else:
            for patron in self.patrons.values():
                patron.display_patron()




library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Display All Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")

        patron = Patron(patron_id, name)
        library.register_patron(patron)

    elif choice == "3":
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        library.borrow_book(book_id, patron_id)

    elif choice == "4":
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        library.return_book(book_id, patron_id)

    elif choice == "5":
        library.display_books()

    elif choice == "6":
        library.display_patrons()

    elif choice == "7":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")