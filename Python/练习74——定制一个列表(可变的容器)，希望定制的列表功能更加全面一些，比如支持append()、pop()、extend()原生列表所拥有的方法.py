#定制一个列表，要求记录列表中每个元素被访问的次数，同时希望定制的列表能支持append()、pop()、extend()原生列表所拥有的方法
#要求1：实现获取、设置和删除一个元素的行为（删除一个元素的时候对应的计数器也会被删除）
#要求2：增加counter(index)方法，返回index参数所指定的元素次数的访问次数
#要求3：实现append()、pop()、remove()、insert()、clear()和reverse()方法（重写这些方法时注意考虑计数器的对应改变）

class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):  # 根据下标返回访问的次数#返回列表元素出现的次数
        return self.count[key]

    def append(self, value):#表示追加至列表结尾
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):#默认后面删除，列表没有元素会报错
        del self.count[key]
        return super().pop(key)

    def remove(self, value):#当列表出现多个相同的值时，删除第一个
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):#指定位置插入元素
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):#删除列表所有元素 
        self.count.clear()
        super().clear()

    def reverse(self):#是列表的内置方法，无参数，无返回值，会改变列表（原地反转）
        self.count.reverse()
        super().reverse()


c1 = CountList(1, 2, 3, 4, 5, 6)
c1[1]
c1[1]
c1[1]
print(c1)
print(c1.count)
print("*"*30)
print(c1.counter(1))
print("*"*30)
c1.append(99)
print(c1)
print(c1.count)
print("*"*30)
c1.pop()
print(c1)
print(c1.count)
print("*"*30)
c1.remove(5)
print(c1)
print(c1.count)
print("*"*30)
c1.insert(2, 55)
print(c1)
print(c1.count)
print("*"*30)
c1.reverse()
print(c1)
print(c1.count)
print("*"*30)
c1.clear()
print(c1)
print(c1.count)

