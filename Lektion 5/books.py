def borrow_books(*books):
    print("Du har lånt " + str(len(books)) + " bøger.")
    for book in books:
        print(book)

def sum_af_lister(liste):
    output_sum = 0
    for nummer in liste:
        output_sum+=nummer
    return output_sum