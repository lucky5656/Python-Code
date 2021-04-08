#玩家和电脑猜拳游戏
#选择角色1 小甲鱼 2海顿上校  3 玩家输入的名字
#角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字
#电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果，本局对战结果...赢...输,是否继续？
#输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束
import random

class Character():                                                                                        #定义角色
        def __init__(self):
                print("-----------野球拳大战-------------\n")
                name=""
                temp = input("请输入你的大名：")
                
                while True:
                        game_character = input(f"请选择你的角色：\n\n1--小甲鱼 2--海顿上校 3--{temp}--->:")
                        if game_character.isdigit():
                                game_character = int(game_character)
                                if game_character == 1:
                                        print("玩家角色为---小甲鱼")
                                        self.name = "小甲鱼"
                                        break
                                elif game_character == 2:
                                        print("玩家角色为---海顿上校")
                                        self.name = "海顿上校"
                                        break
                                elif game_character == 3:
                                        print(f"玩家角色为---{temp}")
                                        self.name = temp
                                        break
                                else:
                                        print("----角色选择错误，请重新进行选择----\n")
                        else:
                                print("----输入角色有误！请重新输入人物序号----\n")
                
                
        def pick_up(self):                                                                                #定义玩家选择
                while True:
                        player_select = input("请输入要出拳的选项：\n1---石头； 2---剪刀； 3---布 :")
                        if player_select.isdigit():
                                player_select = int(player_select)
                                if player_select == 1:
                                        print("玩家选择出---石头", )
                                        break
                                elif player_select == 2:
                                        print("玩家选择出---剪刀")
                                        break
                                elif player_select == 3:
                                        print("玩家选择出--- 布")
                                        break
                                else:
                                        print("选择错误！请重新选择！：",end = " ")
                        else:
                                print("输入数字不正确！请重新输入!:",end = " ")
                return player_select
 
class Computer():                                                                #电脑随机出数
        def random_select(self):
                select_number = random.randint(1,3)
                if select_number == 1:
                        print("电脑选择出---石头")
                elif select_number == 2:
                        print("电脑选择出---剪刀")
                else:
                        print("电脑选择出--- 布")
                return select_number
 
 
class Progress ():                                        #主程序判断
    guesstime1 = 0
    guesstime2 = 0
    guesstime3 = 0
    def __init__(self):
        crct = Character()      
        cmpt = Computer()           
        while True:
            player_result = crct.pick_up()
            computer_result = cmpt.random_select()
            if (player_result == 1 and computer_result == 2 )or \
               (player_result == 2 and computer_result == 3 )or \
               (player_result == 3 and computer_result == 1 ):
                print("---玩家赢---!")
                self.guesstime1 += 1
            elif player_result == computer_result:
                print("---平局！---")
                self.guesstime3 += 1
            else:
                print("---电脑赢！---")
                self.guesstime2 += 1
            if input("**********是否继续?(n键退出，任意键继续)**********").lower()=="n":
                break
        if self.guesstime1 > self.guesstime2:
            final_result="玩家胜利！"
        elif self.guesstime1 == self.guesstime2:
            final_result="平---局!"
        else:
            final_result ="电脑胜利!"
        print("-----------------野球拳大战----------------\n游戏结束 ：\n"
            f"玩家共赢{self.guesstime1}次---电脑共赢{self.guesstime2}次---平局次数{self.guesstime3}次\n————总结果为 ： {final_result}")

gamestart = Progress()
