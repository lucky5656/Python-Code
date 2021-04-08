#在gui4的基础上增强功能：当用户点击OK按钮的时候，比较当前文件是否修改过，如果修改过，则提示覆盖保存,放弃保存或另存为并实现相应功能。

import easygui as g
import os

file_path = g.fileopenbox(default='*.txt')

with open(file_path) as old_file:
    title = os.path.basename(file_path)
    msg = '文件【%s】的内容如下：' % title
    text = old_file.read()
    text_after = g.textbox(msg,title,text)#easygui.textbox函数会在返回的字符串后边追加一个行结束符（“\n”），即print一下就能看见后面多了一个\n，
                                          #而没有print出来的但是已经被调用的则是单纯的字符串没有\n，如果要比较字符串是否发生了改变我们需要人工的把这个\n给忽略掉。
                                          #所以说“字符串[-1]”恰好就是这个\n

if text != text_after[:-1]: #textbox的返回值会在末尾追加一个换行符    #os里的read()输出是一个大的字符串，那么这个大的"字符串[：-1]"就是一个仅仅少一个最后一个字符而已
    choice = g.buttonbox('检测到文件内容发生改变，请选择以下操作：','警告',('覆盖保持','放弃保存','另存为...'))
    if choice == '覆盖保存':
        with open(file_path,'w') as old_file:
            old_file.write(text_after[:-1])
    if choice == '放弃保存':
        pass
    if choice == '另存为...':
        another_path = g.filesavebox(default='.txt')
        if os.path.splitext(another_path)[1] != '.txt':
            another_path += '.txt'
        with open(another_path,'w') as new_file:
            new_file.write(text_after[:-1])
