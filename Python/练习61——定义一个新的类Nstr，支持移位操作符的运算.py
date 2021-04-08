#移位操作符是应用于二进制操作数的，现在定义一个新的类Nstr，也支持移位操作符的运算。

class Nstr(str):
    def __lshift__(self,other):
        return self[other:] + self[:other] #0 1 2  3 ...
    def __rshift__(self,other):
        return self[-other:] + self[:-other]#... -3 -2 -1
