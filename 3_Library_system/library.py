"""
3.Develop a Python program for managing library resources efficiently. Design a class named `LibraryBook` with attributes lie book name, author, and availability status. Implement methods for borrowing  and
returning books while ensuring proper encapsulation of attributes.

Tasks
- Create the `LibraryBook` class with encapsulated attributes
- Implement methods for borrowing and returning books
- Ensure proper encapsulation to protect book details
- Test the borrowing and returning functionality with sample data.
"""

class LibraryBook:
    def __init__(self, book_name, author):
        self.__book_name = book_name
        self.__author = author
        self.__is_available = True

    # Getter methods
    def get_book_name(self):
        return self.__book_name

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__is_available

    # Method for borrowing a book
    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            print(f"The book '{self.__book_name}' by {self.__author} has been borrowed.")
        else:
            print(f"Sorry, the book '{self.__book_name}' by {self.__author} is currently not available.")

    # Method for returning a book
    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"The book '{self.__book_name}' by {self.__author} has been returned.")
        else:
            print(f"The book '{self.__book_name}' by {self.__author} was not borrowed.")

    # Method to display book information
    def display_info(self):
        availability = "available" if self.__is_available else "not available"
        print(f"Book Name: {self.__book_name}")
        print(f"Author: {self.__author}")
        print(f"Availability: {availability}")

# Testing the implemented functionality
if __name__ == "__main__":
    # Create instances of the LibraryBook class
    book1 = LibraryBook("1984", "George Orwell")
    book2 = LibraryBook("To Kill a Mockingbird", "Harper Lee")

    # Display book information
    print("Book 1 Information:")
    book1.display_info()

    print("\nBook 2 Information:")
    book2.display_info()

    # Borrow and return books
    print("\nBorrowing Book 1...")
    book1.borrow_book()
    
    print("\nTrying to borrow Book 1 again...")
    book1.borrow_book()

    print("\nReturning Book 1...")
    book1.return_book()
    
    print("\nTrying to return Book 1 again...")
    book1.return_book()

    # Display updated book information
    print("\nUpdated Book 1 Information:")
    book1.display_info()
