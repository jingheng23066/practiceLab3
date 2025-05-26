book_data = [
    {"title": "1984", "author": "George Orwell", "copies": 12, "price": 15.0},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 8, "price": 12.5},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 5, "price": 10.0},
    {"title": "Brave New World", "author": "Aldous Huxley", "copies": 10, "price": 14.0}
]

def get_books_by_author(author):
    result = []
    for book in book_data:
        if book["author"] == author:
            result.append(book)
    return result

def calculate_total_value():
    total = 0
    for book in book_data:
        total += book["copies"] * book["price"]
    return round(total, 2)

def get_books_below_price(price_limit):
    result = []
    for book in book_data:
        if book["price"] < price_limit:
            result.append(book)
    return result
