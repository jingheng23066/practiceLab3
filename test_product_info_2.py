import product_info_2 as prodInfo

def test_get_products_below_price():
    result = prodInfo.get_products_below_price(301)
    exp_result = [
        {"name": "Mouse", "price": 25, "stock": 100},
        {"name": "Keyboard", "price": 45, "stock": 50},
        {"name": "Monitor", "price": 300, "stock": 20}
    ]
    assert (result == exp_result)

def test_calculate_total_inventory_value():
    result = prodInfo.calculate_total_inventory_value()
    assert (result == 16750)

