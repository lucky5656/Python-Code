import os

all_files = os.listdir(os.curdir)#listdir()-列举指定目录中的文件名，使用os.curdir指代当前目录
file_dict = dict()

for each_file in all_files:
    if os.path.isfile(each_file):#os.path.isfile()函数判断某一路径是否为文件
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size

for each in file_dict.items():#item()方法把字典中每对key和value组成一个元组，并把这些元组放在列表中返回
    print('%s【%dBytes】' %(each[0],each[1]))#each[0]字典中对应key,each[1]为字典中对应value
    
