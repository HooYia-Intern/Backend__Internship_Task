def display_books():
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
