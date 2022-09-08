class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self,book:Book):
        self.books = []
        self.books.append(book)

    def find_book(self,title):
        for book in self.books:
            if book.title == title:
                return f'{book.title} {book.location} {book.author}'

book = Book('asd','ivan','gore')
library = Library(book)
print(library.find_book('asd'))
