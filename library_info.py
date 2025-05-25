library_data = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988, "copies": 5},
    {"title": "1984", "author": "George Orwell", "year": 1949, "copies": 2},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "copies": 4},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "copies": 3}
]

def get_books_by_author(author_name):
    return [book for book in library_data if book["author"] == author_name]

def get_total_copies():
    return sum(book["copies"] for book in library_data)

def get_books_before_year(year):
    return [book for book in library_data if book["year"] < year]

def add_new_book(book):
    if not all(k in book for k in ["title", "author", "year", "copies"]):
        raise ValueError("Book dictionary is missing required keys.")
    library_data.append(book)
