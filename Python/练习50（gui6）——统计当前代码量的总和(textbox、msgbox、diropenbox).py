#写一个程序统计你当前代码量的总和，并显示离十万行代码量还有多远？
#要求1：递归搜索各个文件夹
#要求2：显示各个类型的源文件和源代码数量
#要求3：显示总行数与百分比

#思路：
#1:通过serch_file函数查找当前目录下是否存在target扩展名文件；
#2:存在的话，serch_file函数调用calc_code函数统计文件行数；统计完的数值赋值给变量lines；
#3:文件的类型和源代码行数的数量根据ext的存在而变化。调用递归，搜索上一层。
#4:调用show_result显示打印结果。

import easygui as g
import os

def show_result(start_dir):
    lines = 0
    total = 0
    text = ""

    for i in source_list:
        lines = source_list[i]  #i的结果是ext类型结果的自增lines
        total += lines    #total的结果是souce_list中所有元素的合
        text += "【%s】源文件 %d 个，源代码 %d 行\n" % (i, file_list[i], lines)
    title = '统计结果'
    msg = '您目前共累积编写了 %d 行代码，完成进度：%.2f %%\n离 10 万行代码还差 %d 行，请继续努力！' % (total, total/1000, 100000-total)
    g.textbox(msg, title, text)

def calc_code(file_name):
    lines = 0
    with open(file_name) as f:
        print('正在分析文件：%s ...' % file_name)
        try:
            for each_line in f:
                lines += 1
        except UnicodeDecodeError:
            pass # 不可避免会遇到格式不兼容的文件，这里忽略掉......
    return lines

def search_file(start_dir) :
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir) :
        ext = os.path.splitext(each_file)[1]    #当前目录存在文件的扩展名
        if ext in target :               #如果ext在target字典中
            lines = calc_code(each_file)   # 统计行数
            # 还记得异常的用法吗？如果字典中不存，抛出 KeyError，则添加字典键
            # 统计文件数
            try:
                file_list[ext] += 1       #文件数自增1
            except KeyError:
                file_list[ext] = 1
            # 统计源代码行数
            try:
                source_list[ext] += lines       #行数自增lines，lines来源自calc_code函数
            except KeyError:
                source_list[ext] = lines

        if os.path.isdir(each_file) :             #如果当前搜索的是个目录
            search_file(each_file)   # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录，避免显示空目录和死循环，往上一层搜索

target = ['.c', '.cpp', '.py', '.cc', '.java', '.pas', '.asm']
file_list = {}
source_list = {}

g.msgbox("请打开您存放所有代码的文件夹", "统计代码量")
path = g.diropenbox("请选择您的代码库：")

search_file(path)
show_result(path)
