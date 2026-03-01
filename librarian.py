import json
import os

library_file = "library.json"

def load_library():
    if os.path.exists(library_file):
        file = open(library_file, "r", encoding="utf-8")  
        data = file.read()              
        file.close()                   
        return json.loads(data)     
    return {}

def save_library(library):
    file = open(library_file, "w",encoding="utf-8")     
    file.write(json.dumps(library, indent=4))  
    file.close() 

def add_book(library: dict, title: str, author: str, isbn: str):
    if isbn in library:
        print("This book already exists")
    else:
        library[isbn] = {
            "title": title,
            "author": author,
            "isbn": isbn,
            "available": True
        }
        save_library(library)
        print("Book added successfully!")

def remove_book(library: dict, isbn: str):
    if isbn in library:
        del library[isbn]
        save_library(library)
        print("Book removed successfully!")
    else:
        print("This book not found")

def check_out_book(library: dict, isbn: str):
    if isbn not in library:
        print("This book not found")
    elif not library[isbn]["available"]:
        print("Book is already checked out")
    else:
        library[isbn]["available"] = False
        save_library(library)
        print("Book checked out successfully!")

def return_book(library: dict, isbn: str):
    if isbn in library:
        library[isbn]["available"] = True
        save_library(library)
        print("Book returned successfully!")
    else:
        print("This book not found")

def display_books(library):
    if not library:
        print("No books in the library.")
    for book in library.values():
        status = "Available" if book["available"] else "Checked Out"
        print(f'{book["title"]} by {book["author"]} '
              f'(ISBN: {book["isbn"]}) - {status}')

def search_books(library, keyword):
    found = False
    for book in library.values():
        if keyword.lower() in book["title"].lower() or keyword.lower() in book["author"].lower():
            status = "Available" if book["available"] else "Checked Out"
            print(f'{book["title"]} by {book["author"]} '
                  f'(ISBN: {book["isbn"]}) - {status}')
            found = True
    if not found:
        print("No matching books found.")