import easygui as g
import sys

while 1:
    g.msgbox('嗨，欢迎进入第一个界面小游戏^_^')
    msg = "请问您希望可以学到什么知识呢？"
    title = "小游戏互动"
    choices = ["编程","demo","算法","理论知识"]
    choice = g.choicebox(msg,title,choices)
    g.msgbox("您的选择是：" + str(choice), "结果")
    msg = "您希望重新开始小游戏吗？"
    title = "请选择"
    if g.ccbox(msg,title):  #show a Continue/Cancel dialog
        pass  #user chose Continue
    else:
        sys.exit(0)  #user chose Cancel
