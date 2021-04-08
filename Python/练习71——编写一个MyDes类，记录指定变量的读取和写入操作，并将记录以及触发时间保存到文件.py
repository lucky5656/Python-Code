#编写描述符MyDes：记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件。

import time

class Record:
    def __init__(self, initval=None, name='x'):
        self.val = initval
        self.name = name
        self.filename = "record.txt"

    def __get__(self, instance, owner):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write("%s 变量于北京时间 %s 被读取，%s = %s\n" % \
                    (self.name, time.ctime(), self.name, str(self.val)))
        return self.val

    def __set__(self, instance, value):
        filename = "%s_record.txt" % self.name
        with open(self.filename, 'a', encoding='utf-8') as f: #open(路径+文件名, 读写模式, 编码)a :追加
                                                              #将字符串以utf-8格式保存在txt文件中
            f.write("%s 变量于北京时间 %s 被修改，%s = %s\n" % \
                    (self.name, time.ctime(), self.name, str(value)))
        self.val = value

class Test:
    x = Record(10,'x')
    y = Record(8.8,'y')
