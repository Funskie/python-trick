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
    assert(1 == 2, 'it should fail!')
    return 'but it worked!'
print(error_assert())#but is work!

# 2-3文脈管理器context manager, 讓自己的class也支援with的用法，可以再run完後自動釋放資源，
# 需再class中加入__enter__(), __exit()__方法
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('hello.txt') as f:
    f.write('hello, world!')
    f.write('bye~')#check the file!!!!

# 利用contextlib工具模組實作
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_file('hello_2.txt') as f:
    f.write('hello, world! again...')#check the file!!!!

#寫一個支援文脈管理器的文字縮排程式
class Indenter:
    def __init__(self):
        self.level = 0
    
    def __enter__(self):
        self.level += 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1
    
    def print(self, text):
        print(' ' * 4 * self.level + text)

with Indenter() as indent:
    indent.print('first')
    with indent:
        indent.print('second')
        with indent:
            indent.print('third')
        indent.print('second')
    indent.print('first')