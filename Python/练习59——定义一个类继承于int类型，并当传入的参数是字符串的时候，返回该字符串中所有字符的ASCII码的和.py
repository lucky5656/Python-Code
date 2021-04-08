#定义一个类继承于int类型，并实现一个特殊功能：当传入的参数是字符串的时候，返回该字符串中所有字符的ASCII码的和（使用ord()获取一个字符的ASCII码值）。

class Nint(int):
    def __new__(cls, arg=0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls, arg)
