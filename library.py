#Library Management System
class Library:
    def __init__(self, list_of_books):
        # Initialize the library with a list of books
        self.available_books = list_of_books

    def display_available_books(self):
        # Display all the available books in the library
        if len(self.available_books) == 0:
            print("No books are currently available.")
        else:
            print("Available books in the library:")
            for book in self.available_books:
                print(book)

    def borrow_book(self, book_name):
        # Borrow a book from the library if available
        if book_name in self.available_books:
            print(f"You have borrowed '{book_name}'. Please return it on time.")
            self.available_books.remove(book_name)
        else:
            print(f"Sorry, '{book_name}' is not available or has already been borrowed.")

    def return_book(self, book_name):
        # Return a borrowed book back to the library
        print(f"Thank you for returning '{book_name}'.")
        self.available_books.append(book_name)

class Student:
    def request_book(self):
        # Request a book to borrow
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def return_book(self):
        # Return a borrowed book
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

def main():
    library = Library(["The Great Gatsby", "1984", "To Kill a Mockingbird", "The Catcher in the Rye", "Pride and Prejudice"])
    student = Student()

    while True:
        print("\n===== Welcome to the Library Management System =====")
        print("1. Display all available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            library.display_available_books()
        elif user_choice == '2':
            requested_book = student.request_book()
            library.borrow_book(requested_book)
        elif user_choice == '3':
            returned_book = student.return_book()
            library.return_book(returned_book)
        elif user_choice == '4':
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
