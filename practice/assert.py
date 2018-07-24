#斷言(assert)為python輔助除錯工具，若斷言條件為真程式會繼續執行; 若條件為假則會跳出AssertionError(exception)

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

shoes = {'name': 'NIKE', 'price': 4000}

print(apply_discount(shoes, 0.3)) #output = 2800 Nice!

print(apply_discount(shoes, 1.5))