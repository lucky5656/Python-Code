#编写一个Counter类，用于实时检测对象有多少个属性
class Counter:
    def __init__(self):
        super().__setattr__('counter', 0)
    def __setattr__(self, name, value):
        super().__setattr__('counter', self.counter + 1)
        super().__setattr__(name, value)
    def __delattr__(self, name):
        super().__setattr__('counter', self.counter - 1)
        super().__delattr__(name)

#>>> c = Counter()
#>>> c.x = 1
#>>> c.counter
#1
#>>> c.y = 1
#>>> c.z = 1
#>>> c.counter
#3
#>>> del c.x
#>>> c.counter
#2
