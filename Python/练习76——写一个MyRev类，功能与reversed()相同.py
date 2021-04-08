#写一个MyRev类，功能与reversed()相同（内置函数reversed(seq)，是返回一个迭代器，是序列seq的逆序显示）

class MyRev:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1
        return self.data[self.index]

myRev = MyRev("Python")
for i in myRev:
    print(i, end=' ')
