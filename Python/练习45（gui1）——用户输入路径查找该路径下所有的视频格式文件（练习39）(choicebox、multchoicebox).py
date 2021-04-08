import easygui as g

target = ['.mp4','.avi','.rmvb','.mkv','.torrent']
vedio_list = []

import os
def serach_file(start_dir,target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            vedio_list.append(os.getcwd() + os.sep +each_file + os.linesep)
        if os.path.isdir(each_file):
            serach_file(each_file,target)
            os.chdir(os.pardir)
start_dir = input('请输入需要查找的目录：')
program_dir = os.getcwd()
serach_file(start_dir,target)

f = open(program_dir + os.sep + 'gui1——vedioList.txt','w')
f.writelines(vedio_list)
f.close()

#g.choicebox(msg='在 【%s】 系列路径下工搜索满足条件的文件如下' % start_dir,choices=vedio_list)


g.multchoicebox(msg='在 【%s】 系列路径下工搜索满足条件的文件如下' % start_dir,choices=vedio_list)
#multchoicebox()函数也是提供一个可选择的列表，与choicebox()不同的是，multchoicebox()支持用户选择0个，1个或者同时选择多个选项。
