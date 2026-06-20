books = {
    "Harry potter" : "Available",
    "Python basics" : "Available",
    "cricket history" : "Available",
}
while True:
    print(f"\n1. view books")
    print(f"2. issue books")
    print(f"3.return books")
    print(f"4.exit")
    choice = input("ch(oose option :")
    if choice== "1":
        for book , status in books.items():
            print(book,"--", status)
    elif choice == "2":
        book_name = input("book name to issue:")
        if book_name in books:
            if books[book_name] == "Available":
                books[book_name] = "issued"
                print(book_name, "issued succesfully!")
            else:
                print("sorry, book is already issued!")
        else :
            print("book not found !")

    elif choice == "3":
        book_name = input("book name to return :")
        if book_name in books:
            books[book_name] = "Available"
            print(book_name, "returned succesfully!")
        else:
            print("book not found")
    elif choice == "4":
        break