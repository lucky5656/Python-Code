# 测试
import Const 

Const.NAME = "Python"
print(Const.NAME)

try:
    # 尝试修改常量
    Const.NAME = "Pycharm"
except TypeError as Err:
    print(Err)

try:
    # 变量名需要大写
    Const.name = "Python"
except TypeError as Err:
    print(Err)
