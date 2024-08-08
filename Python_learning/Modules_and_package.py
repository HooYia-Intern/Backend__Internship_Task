import json
import os

# Initial data
books = []
members = {}

def display_books():
    if not books:
        print("No books available in the library.")
    else:
        print("Books in the library:")
        for book in books:
            print(book)

def is_book_available(book_name):
    return book_name in books

def add_book(book_name):
    if book_name not in books:
        books.append(book_name)
        print(f"Book '{book_name}' added to the library.")
    else:
        print(f"Book '{book_name}' already exists in the library.")

def lend_book(member_name, book_name):
    if is_book_available(book_name):
        if member_name not in members:
            members[member_name] = []
        members[member_name].append(book_name)
        books.remove(book_name)
        print(f"Book '{book_name}' lent to {member_name}.")
    else:
        print(f"Book '{book_name}' is not available.")

def get_member_books(member_name):
    try:
        return members[member_name]
    except KeyError:
        print(f"Member '{member_name}' does not exist.")
        return []

def save_library_data():
    data = {"books": books, "members": members}
    with open("library_data.json", "w") as file:
        json.dump(data, file)
    print("Library data saved.")

def load_library_data():
    global books, members
    try:
        with open("library_data.json", "r") as file:
            data = json.load(file)
            books = data["books"]
            members = data["members"]
        print("Library data loaded.")
    except FileNotFoundError:
        print("No saved library data found.")

def main():
    load_library_data()

    while True:
        print("\nLibrary Menu")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Lend Book")
        print("4. View Member's Books")
        print("5. Save & Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            display_books()
        elif choice == "2":
            book_name = input("Enter the book name: ").strip()
            add_book(book_name)
        elif choice == "3":
            member_name = input("Enter the member's name: ").strip()
            book_name = input("Enter the book name: ").strip()
            lend_book(member_name, book_name)
        elif choice == "4":
            member_name = input("Enter the member's name: ").strip()
            books = get_member_books(member_name)
            if books:
                print(f"Books borrowed by {member_name}: {', '.join(books)}")
            else:
                print(f"{member_name} has not borrowed any books.")
        elif choice == "5":
            save_library_data()
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
