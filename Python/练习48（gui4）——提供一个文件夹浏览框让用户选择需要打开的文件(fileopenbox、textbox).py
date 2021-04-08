#提供一个文件夹浏览框，让用户选择需要打开的文件，打开并显示文件内容
import easygui as g
import os

file_path = g.fileopenbox(default="*.txt")

with open(file_path) as f:
    title = os.path.basename(file_path)#os.path.basename(),返回path最后的文件名
    msg = "文件【%s】的内容如下：" % title
    text = f.read()
    g.textbox(msg, title, text)
