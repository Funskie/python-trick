#2-1斷言(assert)為python輔助除錯工具，若斷言條件為真程式會繼續執行; 若條件為假則會跳出AssertionError(exception)

def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

shoes = {'name': 'NIKE', 'price': 4000}

print(apply_discount(shoes, 0.3)) #output = 2800 Nice!

#print(apply_discount(shoes, 1.5))
'''
斷言跳出例外：
Traceback (most recent call last):
  File "/Users/funskie/Desktop/python-trick-master/practice/assert.py", line 12, in <module>
    print(apply_discount(shoes, 1.5))
  File "/Users/funskie/Desktop/python-trick-master/practice/assert.py", line 5, in apply_discount
    assert 0 <= price <= product['price']
AssertionError
'''
#assert 用在程式內部自我檢查，若是可預期的情況(ex: 條件描述、找不到檔案...)則使用if或自定義的Error
#當tuple為assert第一個參數時，條件一定為真，所以斷言不可能會work
def error_assert():
    assert(1 == 2, 'it should fail!')#but is work!
    pass
error_assert()