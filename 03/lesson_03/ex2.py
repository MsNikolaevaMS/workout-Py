from book import Book

library = []

# Наполняем список тремя экземплярами класса Book
library.append(Book("1984", "George Orwell"))
library.append(Book("To Kill a Mockingbird", "Harper Lee"))
library.append(Book("The Great Gatsby", "F. Scott Fitzgerald"))

# Цикл для печати всей библиотеки в нужном формате
for book in library:
    print(f"{book.name} - {book.author}")
