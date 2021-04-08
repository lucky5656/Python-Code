#按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
#平日票价100元
#周末票价为平日的120%
#儿童半票

class Ticket:
    def __init__(self,weekend=False,child=False):
        self.price = 100
        if weekend:
            self.increase = 1.2
        else:
            self.increase = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self,num):
        return self.price * self.increase * self.discount * num

adult = Ticket()
child  = Ticket(child=True)
print("2个大人 + 1个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))

adult2 = Ticket(weekend=True)
child2 = Ticket(weekend=True, child=True)
print("2个大人 + 1个小孩周末票价为：%.2f" % (adult2.calcPrice(2) + child2.calcPrice(1)))
