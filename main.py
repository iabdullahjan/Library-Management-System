books = []


def add_book():
    title = input("Enter book title: ")

    if title == "":
        print("Book title cannot be empty")

    else:
        books.append(title)
        print("Book added successfully")


def view_books():

    if len(books) == 0:
        print("No books available")

    else:
        print("\nBooks in Library:")

        for book in books:
            print(book)


def search_book():

    title = input("Enter book title to search: ")

    if title in books:
        print("Book found")

    else:
        print("Book not found")


def delete_book():

    title = input("Enter book title to delete: ")

    if title in books:
        books.remove(title)
        print("Book deleted successfully")

    else:
        print("Book not found")


while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()

    elif choice == '2':
        view_books()

    elif choice == '3':
        search_book()

    elif choice == '4':
        delete_book()

    elif choice == '5':
        print("Program exited")
        break

    else:
        print("Invalid choice")