#定义一个类，当实例化该类的时候，自动判断传入了多少个参数，并显示出来。

class C:
    def __init__(self, *args):
        if not args:
            print("并没有传入参数")
        else:
            print("传入了%d个参数，分别是：" % len(args), end=' ')
            for each in args:
                print(each, end=' ')
