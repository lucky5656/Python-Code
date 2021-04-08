import os

all_files = os.listdir(os.curdir)#listdir()-列举指定目录中的文件名，使用os.curdir指代当前目录
type_dict = dict() #创建一个字典

for each_file in all_files:
    if os.path.isdir(each_file): #isdir判断指定路径是否存在且是一个目录
                                 #判断each_file路径是否是一个文件夹
        type_dict.setdefault('文件夹',0)
        type_dict['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]#这里的分割是带点的，如：.txt
                                            #分离文件名与后缀名 [0]文件名,[1]后缀名
        type_dict.setdefault(ext,0)
        type_dict[ext] += 1

for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件%d个'%(each_type,type_dict[each_type]))
    
