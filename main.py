import librarian


library = librarian.load_library() 

while True:
    print("\n=== Library Menu ===")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Borrow (Check Out) Book")
    print("6. Return Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter author: ")
        isbn = input("Enter ISBN: ")
        librarian.add_book(library, title, author, isbn)
    elif choice == "2":
        librarian.display_books(library)
    elif choice == "3":
        keyword = input("Enter title or author to search: ")
        librarian.search_books(library, keyword)
    elif choice == "4":
        isbn = input("Enter ISBN to delete: ")
        librarian.remove_book(library, isbn)
    elif choice == "5":
        isbn = input("Enter ISBN to borrow: ")
        librarian.check_out_book(library, isbn)
    elif choice == "6":
        isbn = input("Enter ISBN to return: ")
        librarian.return_book(library, isbn)
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")