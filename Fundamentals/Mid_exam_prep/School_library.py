shelf = input().split("&")

while True:
    command = input().split(" | ")
    if command[0] == "Done":
        print(", ".join(shelf))
        break

    if command[0] == "Add Book":
        book = command[1]
        if book not in shelf:
            shelf.insert(0, book)
    elif command[0] == "Take Book":
        book_name = command[1]
        if book_name in shelf:
            shelf.remove(book_name)
    elif command[0] == "Swap Books":
        book1 = command[1]
        book2 = command[2]
        if book1 in shelf and book2 in shelf:
            index_book1 = shelf.index(book1)
            index_book2 = shelf.index(book2)
            shelf[index_book1], shelf[index_book2] = shelf[index_book2], shelf[index_book1]
    elif command[0] == "Insert Book":
        book_ind = command[1]
        shelf.append(book_ind)
    elif command[0] == "Check Book":
        ind_book = int(command[1])
        if 0 <= ind_book < len(shelf):
            print(shelf[ind_book])








