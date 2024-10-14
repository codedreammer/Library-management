library = []

while True:
    print("\nLibrary Menu:")
    print("1. Add a book")
    print("2.Remove a book")
    print("3.Display all books")
    print("4.Exit")

    code= complex(input("Enter your Library code:"))
    choice= input("Enter your choice:")

    if choice == '1':
        book = input("Enter the name of the book to add: ")
        library.append(book)
        print(f"'{book}' has been added to the library.")
    
    elif choice == '2':
        book = input("Enter the name of the book to remove: ")
        if book in library:
            library.remove(book)
            print(f"'{book}' has been removed from the library.")

        else:
            print(f"'{book}' not found in the library.")

    
    elif choice == '3':
        if library:
            print("Books available in the library:")
            for b in library:
                print(f"- {b}")
        else:
            print("No books available in the library.")
            
    elif choice == '4':
        print("Exiting the library system. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")    
