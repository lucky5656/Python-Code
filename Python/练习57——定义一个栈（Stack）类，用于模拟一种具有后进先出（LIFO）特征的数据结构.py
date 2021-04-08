#定义一个栈（Stack）类，用于模拟一种具有后进先出（LIFO）特征的数据结构。
#至少需要有以下办法：
# 方法名 	含义
# isEmpty() 	判断当前栈是否为空（返回True或False）
# push() 	往栈的顶部压入一个数据项
# pop() 	从栈顶弹出一个数据项（并在栈中删除）
# top() 	显示当前栈顶的一个数据项
# bottom() 	显示当前栈底的一个数据项

class Stack():
    def __init__(self, start=[]):#1、为啥开始要赋值个start为空列表的默认值，而下面又用了个self.stack变量为空的列表？
                                 #形参和实参的关系。定义类时start是形参，实例化之后self.stack就是实参了；
                                 #因为是列表，下面操作的一系列相关都是针对列表的操作（增减），所以需要复制一份列表出来。
        
        self.stack = []          #2、为啥要定义栈为空？
                                 #因为一系列的增减都是针对列表的，当列表为空的时候，是没办法索引的。
        
        for x in start:          #3、为啥要用个for循环？直接self.push(x)不行吗？
            self.push(x)         #for循环是为了保证你实例化时传入非空列表进行迭代用。
                                 #传入的实参分两种情况，一种是空列表【 】；一种是带元素的列表，如【1，2，3，4，5】。
                                 #比如c=Stack([1,2,3,4,5]) print(c.stack)这一种情况想要压栈的话，就必须一个个压进去，for循环的作用就在这了。


    def isEmpty(self):  # 判断是否为空
        return not self.stack

    def push(self, obj):  # 入栈
        print("成功入栈数据：", obj)
        self.stack.append(obj)

    def pop(self):  # 出栈
        if not self.stack:
            print("警告：栈为空！")
        else:
            print("成功出栈数据：", self.stack[-1])
            return self.stack.pop()

    def top(self):  # 显示第一个栈顶数据
        if not self.stack:
            print("警告：栈为空！")
        else:
            print("栈顶数据为：", end="")
            return self.stack[-1] #取出目前stack中最新的元素#index倒1，最后一位元素

    def bottom(self):  # 显示栈底数据
        if not self.stack:
            print("警告：栈为空！")
        else:
            print("栈底数据为：", end="")
            return self.stack[0]

    def showStack(self): # 展示栈内的所有数据（自己附加上去的方法，为了方便看栈内还有哪些数据）
        print("目前栈内的所有数据为：", end="")
        return self.stack[:]


s = Stack([])
print('当前栈是否为空：', s.isEmpty())  # True
s.push('1')
s.push('2')
s.push('3')
s.push('4')
s.push('5')
s.push('6')
print(s.showStack())
print(s.top())  # 栈顶是5
s.pop()  # 5被弹出，栈顶变成4
print(s.showStack())
print(s.top())
print(s.bottom())
