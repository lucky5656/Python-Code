#定义一个点（Point）类和直线（Line）类，使用getLen方法可以获得直线的长度。
#提示：
#1.设点A(X1,Y1)、B(X2,Y2)，则两点构成的直线长度为|AB| = √(X1-X2)^2 + (Y1-Y2)^2
#2.ython中计算开根号可使用math模块中的sqrt函数
#3.直线需有两点构成，因此初始化时需要有两个点（Point）对象作为参数


import math

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class Line():
    def __init__(self, p1, p2):
        self.x = p1.getX() - p2.getX()
        self.y = p1.getY() - p2.getY()

    def getLen(self):
        self.len = math.sqrt(self.x * self.x + self.y * self.y)
        return self.len

p1 = Point(1, 1)
p2 = Point(4, 4)
line = Line(p1, p2)
print(line.getLen())
