#定义一个类Nstr，当该类的实例对象间发生的加、减、乘、除运算时，将该对象的所有字符串的ASCII码之和进行运算。

class Nstr(str):
    def __init__(self,arg=''):
        if isinstance(arg,str):
            self.total = 0
            for each in arg:
                self.total += ord(each)
        else:
            print("参数错误")

    def __add__(self,other):
        return self.total + other.total

    def __sub__(self,other):
        return self.total - other.total

    def __mul__(self,other):
        return self.total * other.total

    def __truediv__(self,other):
        return self.total / other.total

    def __floordiv__(self,other):
        return self.total // other.total
