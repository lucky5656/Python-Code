#定义一个单词（Word）类继承自字符串，重写比较操作符，当两个Word类对象进行比较时，根据单词的长度来进行比较大小。
#加分要求：实例化时如果传入的是带空格的字符串，则取第一个空格前的单词作为参数。
#加分要求可以通过重载__ new__方法来实现（因为字符串是不可变类型），通过重写__ gt__、__ lt__、__ ge__、__ le__方法来定义Word类在比较操作中的表现。

class Word(str):
    '''存储单词的类，定义比较单词的几种方法'''
    def __new__(cls, word):
        # 注意我们必须要用到__new__方法，因为str是不可变类型
        # 所以我们必须在创建的时候将它初始化
        if ' ' in word:
            print("Value contains spaces. Truncating to first space.")
            word = word[:word.index(' ')]  # 单词是第一个空格之前的所有字符
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return  len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)
            
w1 = Word('abcd')
w2 = Word('abca vsdv')
if w1 >= w2:
    print(True)
else:
    print(False)
