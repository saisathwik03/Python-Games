import json

def load_books():
    books = []
    filename = 'books.json'
    if filename:
        with open(filename, 'r') as file:
            data = json.load(file)
            for book in data:
                books.append(book)
    else:
        print("File 'books.json' not found.")
    return books

def save_books(books):
    filename = 'books.json'
    with open(filename, 'w') as file:
        json.dump(books, file)

def add_book(books):
    new_book = {}
    new_book['title'] = input('Enter the title to add: ')
    new_book['author'] = input('Enter the author to add: ')
    new_book['year'] = int(input('Enter the year: '))
    new_book['genre'] = input('Enter the genre of the book: ')
    books.append(new_book)
    save_books(books)

def view_collection(books):
    print("Your book collection:")
    for book in books:
        print(book)

def search_books(books):
    title = input("Enter title to search: ")
    for book in books:
        if book['title'].lower() == title.lower():
            print(book)
    
    print('Book not found by title, searching by author...')
    
    author = input("Enter author to search: ")
    for book in books:
        if book['author'].lower() == author.lower():
            print(book)
    
    return 'Book not found in Books Collection !!'


def remove_book(books):
    title = input("Enter title to search: ")
    for book in books:
        if book['title'].lower() == title.lower():
            books.remove(book)
            return books
    return 'Book not found in Books Collection to remove !!'

def sort_collection(books):
    print("Choose an option to sort by:")
    print("1. Title")
    print("2. Author")
    print("3. Year of publication")
    
    option = int(input("Enter your choice (1/2/3): "))
    
    if option == 1:
        for i in range(len(books)):
            for j in range(i + 1, len(books)):
                if books[i]['title'] > books[j]['title']:
                    books[i], books[j] = books[j], books[i]
    elif option == 2:
        for i in range(len(books)):
            for j in range(i + 1, len(books)):
                if books[i]['author'] > books[j]['author']:
                    books[i], books[j] = books[j], books[i]
    elif option == 3:
        for i in range(len(books)):
            for j in range(i + 1, len(books)):
                if books[i]['year'] > books[j]['year']:
                    books[i], books[j] = books[j], books[i]
    else:
        print("Invalid choice, returning unsorted collection.")
        print(books)

    print(books)  

def collections():
    print('Welcome to your Book Collections !!!')
    books = load_books()
    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. View Collection")
        print("3. Search Books")
        print("4. Remove Book")
        print("5. Sort Collection")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book(books)
        elif choice == '2':
            view_collection(books)
        elif choice == '3':
            search_books(books)
        elif choice == '4':
            remove_book(books)
        elif choice == '5':
            sort_collection(books)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

collections()