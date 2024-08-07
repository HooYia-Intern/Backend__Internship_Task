import sqlite3
import uuid
from abc import ABC, abstractmethod

# Function to create the SQLite3 database and book table if they do not exist
def create_database():
    conn = sqlite3.connect('library_management.db')  # Connect to the database
    cursor = conn.cursor()  # Create a cursor object
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            unique_id TEXT UNIQUE,
            title TEXT,
            author TEXT,
            publication_date TEXT,
            isbn TEXT,
            pages INTEGER
        )
    ''')  # SQL query to create the books table
    conn.commit()  # Commit the changes
    conn.close()  # Close the connection

# Abstract base class for database operations
class DatabaseOperations(ABC):

    @abstractmethod
    def create_book(self, book):
        pass

    @abstractmethod
    def update_book(self, book_id, updated_book):
        pass

    @abstractmethod
    def delete_book(self, book_id):
        pass

    @abstractmethod
    def retrieve_book(self, book_id):
        pass

    @abstractmethod
    def list_books(self):
        pass

# Book class inheriting from DatabaseOperations
class Book(DatabaseOperations):

    def __init__(self, title, author, publication_date, isbn, pages):
        self.conn = sqlite3.connect('library_management.db')  # Connect to the database
        self.cursor = self.conn.cursor()  # Create a cursor object
        self._unique_id = self.generate_unique_id()  # Generate unique ID
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.isbn = isbn
        self.pages = pages

    @staticmethod
    def generate_unique_id():
        return str(uuid.uuid4())  # Generate a UUID for unique ID

    # Method to insert a new book into the database
    def create_book(self, book):
        self.cursor.execute('''
            INSERT INTO books (unique_id, title, author, publication_date, isbn, pages)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (book._unique_id, book.title, book.author, book.publication_date, book.isbn, book.pages))  # SQL query to insert a book
        self.conn.commit()  # Commit the changes

    # Method to update an existing book's details in the database
    def update_book(self, book_id, updated_book):
        current_book = self.retrieve_book(book_id)
        if not current_book:
            print("Book not found!")
            return
        
        print("Current Book Details:")
        print(f"ID: {current_book[1]}")
        print(f"Title: {current_book[2]}")
        print(f"Author: {current_book[3]}")
        print(f"Publication Date: {current_book[4]}")
        print(f"ISBN: {current_book[5]}")
        print(f"Pages: {current_book[6]}")

        confirm = input("Is this the book you want to update? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Update cancelled.")
            return

        title = input(f"Enter New Title [{current_book[2]}]: ") or current_book[2]
        author = input(f"Enter New Author [{current_book[3]}]: ") or current_book[3]
        publication_date = input(f"Enter New Publication Date (YYYY-MM-DD) [{current_book[4]}]: ") or current_book[4]
        isbn = input(f"Enter New ISBN [{current_book[5]}]: ") or current_book[5]
        pages = input(f"Enter New Pages [{current_book[6]}]: ") or current_book[6]

        self.cursor.execute('''
            UPDATE books
            SET title = ?, author = ?, publication_date = ?, isbn = ?, pages = ?
            WHERE unique_id = ?
        ''', (title, author, publication_date, isbn, pages, book_id))  # SQL query to update a book
        self.conn.commit()  # Commit the changes
        print("Book updated successfully!")

    # Method to delete a book from the database
    def delete_book(self, book_id):
        current_book = self.retrieve_book(book_id)
        if not current_book:
            print("Book not found!")
            return
        
        print("Current Book Details:")
        print(f"ID: {current_book[1]}")
        print(f"Title: {current_book[2]}")
        print(f"Author: {current_book[3]}")
        print(f"Publication Date: {current_book[4]}")
        print(f"ISBN: {current_book[5]}")
        print(f"Pages: {current_book[6]}")

        confirm = input("Is this the book you want to delete? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Delete cancelled.")
            return

        self.cursor.execute('''
            DELETE FROM books WHERE unique_id = ?
        ''', (book_id,))  # SQL query to delete a book
        self.conn.commit()  # Commit the changes
        print("Book deleted successfully!")

    # Method to retrieve a book's details from the database
    def retrieve_book(self, book_id):
        self.cursor.execute('''
            SELECT * FROM books WHERE unique_id = ?
        ''', (book_id,))  # SQL query to retrieve a book
        book = self.cursor.fetchone()  # Fetch the book's details
        return book  # Return the book's details

    # Method to list all books in the database
    def list_books(self):
        self.cursor.execute('''
            SELECT * FROM books
        ''')  # SQL query to list all books
        books = self.cursor.fetchall()  # Fetch all books
        return books  # Return the list of books

    # Method to close the database connection
    def close_connection(self):
        self.conn.close()  # Close the connection

# Function to display the menu and handle user input
def main():
    create_database()  # Ensure the database and table are created

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Retrieve Book")
        print("5. List Books")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            publication_date = input("Enter Publication Date (YYYY-MM-DD): ")
            isbn = input("Enter ISBN: ")
            pages = input("Enter Number of Pages: ")
            book = Book(title, author, publication_date, isbn, int(pages))
            book.create_book(book)
            print("Book added successfully!")
            book.close_connection()  # Close the connection

        elif choice == '2':
            book_id = input("Enter Book Unique ID to Update: ")
            book = Book("", "", "", "", 0)
            book.update_book(book_id, book)
            book.close_connection()  # Close the connection

        elif choice == '3':
            book_id = input("Enter Book Unique ID to Delete: ")
            book = Book("", "", "", "", 0)
            book.delete_book(book_id)
            book.close_connection()  # Close the connection

        elif choice == '4':
            book_id = input("Enter Book Unique ID to Retrieve: ")
            book = Book("", "", "", "", 0)
            retrieved_book = book.retrieve_book(book_id)
            if retrieved_book:
                print("Book Details:")
                print(f"ID: {retrieved_book[1]}")
                print(f"Title: {retrieved_book[2]}")
                print(f"Author: {retrieved_book[3]}")
                print(f"Publication Date: {retrieved_book[4]}")
                print(f"ISBN: {retrieved_book[5]}")
                print(f"Pages: {retrieved_book[6]}")
            else:
                print("Book not found!")
            book.close_connection()  # Close the connection

        elif choice == '5':
            book = Book("", "", "", "", 0)
            books = book.list_books()
            print("All Books:")
            for b in books:
                print(f"ID: {b[1]}, Title: {b[2]}, Author: {b[3]}, Publication Date: {b[4]}, ISBN: {b[5]}, Pages: {b[6]}")
            book.close_connection()  # Close the connection

        elif choice == '6':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()  # Call the main function to run the program
