#用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件（要求查找mp4 rmvb, avi的格式即可），并把创建一个文件（vedioList.txt）存放所有找到的文件的路径。
import os

def search_file(start_dir, target) :
    os.chdir(start_dir)
    
    for each_file in os.listdir(os.curdir) :
        ext = os.path.splitext(each_file)[1]
        if ext in target :
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)  # 使用os.sep是程序更标准
        if os.path.isdir(each_file) :
            search_file(each_file, target)                         # 递归调用
            os.chdir(os.pardir)                                         # 递归调用后切记返回上一层目录

start_dir = input('请输入待查找的初始目录(例如：D:\2019.12六级考试指南\2019.12六级考试指南）：')
program_dir = os.getcwd()

target = ['.mp4', '.avi', '.rmvb']
vedio_list = []

search_file(start_dir, target)

f = open(program_dir + os.sep + '练习39——vedioList.txt', 'w')
f.writelines(vedio_list)
f.close()
