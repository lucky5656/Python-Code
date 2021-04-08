#写一个迭代器，要求输出至今为止的所有闰年

import datetime as dt

class LeapYear:
    def __init__(self):
        self.now = dt.date.today().year #返回一个表示当前本地日期的date对象

    def isLeapYear(self, year):
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        while not self.isLeapYear(self.now):
            self.now -= 1

        temp = self.now
        self.now -= 1

        return temp


ly = LeapYear()
for i in ly:
    if i > 2000:
        print(i)
    else:
        break
