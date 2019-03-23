def borrow_books(*books):
    print("Du har lånt " + str(len(books)) + " bøger.")
    for book in books:
        print(book)


borrow_books("Bibel")

borrow_books("Bibel", "Koran", "Tora")

borrow_books()
