import book_inventory as bi

def test_get_books_by_author():
    result = bi.get_books_by_author("George Orwell")
    expected = [
        {"title": "1984", "author": "George Orwell", "copies": 12, "price": 15.0}
    ]
    assert result == expected

def test_calculate_total_value():
    result = bi.calculate_total_value()
    expected = 470.0
    assert result == expected

def test_get_books_below_price():
    result = bi.get_books_below_price(13.0)
    expected = [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 8, "price": 12.5},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 5, "price": 10.0}
    ]
    assert result == expected