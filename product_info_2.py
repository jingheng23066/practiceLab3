products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 100},
    {"name": "Keyboard", "price": 45, "stock": 50},
    {"name": "Monitor", "price": 300, "stock": 20},
]

def get_products_below_price(max_price):
    return [p for p in products if p["price"] < max_price]

def calculate_total_inventory_value():
    total = 0
    for item in products:
        total += item["price"] * item["stock"]
    return total
