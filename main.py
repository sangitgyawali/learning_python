# Magic Methods in Python

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.num_pages} pages"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("1984", "George Orwell", 328)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 281)

print(book2 < book3)
