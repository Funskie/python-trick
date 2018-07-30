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

#2-4:__ dunder的各種用法
#第一種：前單底線 _var
#為約定成俗用法沒有強制力，代表此變數或方法只限內部使用
class Test:
    def __init__(self):
        self.foo = 11
        self._baz = 23
t = Test()
print(t.foo)#11
print(t._baz)#23
#若使用星號import會忽略前單底線的名稱（除非module裡的__all__串列含有該名稱

#第二種：後單底線 var_
#想用的名稱已被python拿去當關鍵字了衹好後面加個_...
#def make_object(name, class):
#會報SyntaxError: "invalid syntax"
def make_object(name, class_):
    pass

#第三種：前雙底線__var
#Python 直譯器會觸發名稱修飾name mangling避免繼承時有名稱衝突發生
class Test1:
    def __init__(self):
        self.foo = 11
        self._baz = 23
        self.__baz = 24
t1 = Test1()
print(t1.foo)#11
print(t1._baz)#23
#print(t1.__baz) output:AttributeError: 'Test1' object has no attribute '__baz'
print(dir(t1)) #output:['_Test1__baz', '__class__', '__delattr__', '__dict__', '__dir__', 
#'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
# '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
# '__subclasshook__', '__weakref__', '_baz', 'foo']
class Extented_Test1(Test1):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._baz = 'overriden'
        self.__baz = 'overriden'
t2 = Extented_Test1()
print(dir(t2))# output:['_Extented_Test1__baz', '_Test1__baz', '__class__', 
#'__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', 
# '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_baz', 'foo']
_Test3__baz = 23
class Test3:
    def test(self):
        return __baz
t3 = Test3()
print(t3.test())#23

#第四種：前後雙底線__var__
#不會觸發python直譯器，為特殊用途，ex:__init__作為建構子，__call__讓物件可被呼叫

#第五種：單底線_
#有時代表變數是暫時性的或不重要的
for _ in range(3):
    print('Hello, World!')
#Hello, World!
#Hello, World!
#Hello, World!
#也可用於拆箱運算式Unpacking Expression，作為不必在意的變數，這也是慣例不會觸發直譯器
car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
print(color, mileage)#red 3812.4