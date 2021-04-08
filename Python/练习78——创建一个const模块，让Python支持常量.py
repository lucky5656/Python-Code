#创建一个const模块，功能是让Python支持常量

# 该模块用于让Python支持常量操作
class Const:
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise TypeError('常量无法改变！')

        if not name.isupper():
            raise TypeError('常量名必须由大写字母组成！')

        self.__dict__[name] = value

import sys
sys.modules[__name__] = Const()

