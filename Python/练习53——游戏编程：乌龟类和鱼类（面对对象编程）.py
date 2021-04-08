#按以下要求定义一个乌龟类和鱼类并尝试编写游戏。
#游戏场景为范围(x,y)为 0<=x<=10，0<=y<=10
#游戏生成1只乌龟和10条鱼
#它们的移动方向均随机
#乌龟的最大移动能力为2(可以随机选择1还是2),鱼儿的最大移动能力为1
#当移动到场景边缘,自动向反方向移动
#乌龟初始化体力为100（上限）
#乌龟每移动一次,体力消耗1
#当乌龟和鱼坐标重叠,乌龟吃掉鱼，乌龟体力增加20
#鱼暂不计算体力
#当乌龟体力值为0(挂掉)或鱼儿的数量为0游戏结束

import random as r

class Turtle:
    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置随机
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        # 随机计算方向并移动到新的位置(x, y)
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])
        # 检查移动后是否超出场景x轴边界
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y
        # 体力消耗
        self.power -= 1
        # 返回移动后的新位置
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        # 随机计算方向并移动到新的位置(x, y)
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 检查移动后是否超出场景x轴边界
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y
        # 返回移动后的新位置
        return (self.x, self.y)

# 开始测试数据
turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)#这里append的是十只鱼的随机坐标

while True:
    if not len(fish):#len(fish)为零(fish列表为空)，游戏结束
        print("鱼都吃完了，游戏结束！")
        break
    if not turtle.power: #实例化的turtle中power为零，游戏结束
        print("乌龟体力耗尽，挂了！")
        break

    #游戏开始
    #首先乌龟迈出第一步
    print("乌龟移动前坐标：", (turtle.x ,turtle.y)) #乌龟移动前   
    turtle.move()
    print("乌龟移动后坐标：", (turtle.x ,turtle.y)) #乌龟移动后
    for each_fish in fish[:]:
        print("鱼移动前坐标：", (each_fish.x ,each_fish.y))
        each_fish.move()  # 感觉鱼的移动前后的坐标差有问题
        print("鱼移动后坐标：", (each_fish.x ,each_fish.y))
        if each_fish.x==turtle.x and each_fish.y==turtle.y:
            turtle.eat()
            fish.remove(each_fish)
            print("死了一只鱼")
            print("乌龟最新体力值为 %d"%turtle.power)   
