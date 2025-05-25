import library_info as lib

def test_get_books_by_author():
    # Write test logic here
    result = lib.get_books_by_author("Paulo Coelho")
    exp_result = [
        {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1988, "copies": 5}
    ]
    assert (result == exp_result)

def test_get_total_copies():
    # Write test logic here
    result = lib.get_total_copies()
    assert(result == 14)

def test_get_books_before_year():
    result= lib.get_books_before_year(1950)
    exp_result= [
         {"title": "1984", "author": "George Orwell", "year": 1949, "copies": 2},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "copies": 4}
    ]


