#编写一个不可改变的自定义列表，要求记录列表中每个元素被访问的次数。

class Countlist:

    def __init__(self,*args):#初始化,*args表示可增加的参数个数
        self.values = [x for x in args]#用列表推导式遍历用户传入的参数并建立一个列表#self.values里面的内容是用户传入的参数
        self.count = {}.fromkeys(range(len(self.values)),0)#用fromkeys方法建立一个字典,self.count是字典
                                                            #字典的key是self.value的索引，对应value分别初始化为0#建立字典count = {0:0, 1:0, 2:0, 3:0...n:0)，用于存放计数

    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        #注意这里用户若想要得到某个参数的访问次数，需要传入该参数的索引值
        self.count[key] += 1 #每访问一次key对应的value就记录一次
        return self.values[key]
    
