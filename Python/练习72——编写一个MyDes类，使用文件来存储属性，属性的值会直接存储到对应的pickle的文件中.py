#描述符MyDes，使用文件来存储属性，属性的值会直接存储到对应的pickle的文件中。
#如果属性被删除了，文件也会同时被删除，属性的名字也会被注销。

import os
import pickle

class MyDes:
    saved = []

    def __init__(self, name='11'):
        self.name = name
        self.filename = self.name + '.pkl'

    def __get__(self, instance, owner):
        if self.name not in MyDes.saved:
            raise AttributeError("%s 属性还没有赋值！" % self.name)

        with open(self.filename, 'rb') as f:
            value = pickle.load(f)

        return value

    def __set__(self, instance, value):
        with open(self.filename, 'wb') as f:
            pickle.dump(value, f)
            MyDes.saved.append(self.name)

    def __delete__(self, instance):
        os.remove(self.filename)
        MyDes.saved.remove(self.name)

class Test:
    x = MyDes('x')
    y = MyDes('y')
