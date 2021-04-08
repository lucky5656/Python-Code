#编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀）
#要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符）。


import os


#================打印结果==================
#此函数主用于search_files函数需要打印具体位置时，调用此函数将字典类型排序，打印对应行数及位置。

def print_pos(key_dict):
    keys = key_dict.keys()         #分离字典的key
    keys = sorted(keys)            #由于字典是无序的，我们这里对行数进行排序#sorted()函数就可以对list进行排序
    for each_key in keys:
        print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key, str(key_dict[each_key])))


#================在某行查找关键字==================
#此函数主用于定位关键字所在行的位置，返给serch_in_file写入字典value.

def pos_in_line(line, key):
    pos = []
    begin = line.find(key)       #查找关键字在每一行中的位置，赋值给begin #find方法不包含索引值会返回-1
    while begin != -1:           #不为-1时代表找到了，建议了解下find函数。
        pos.append(begin + 1)    # 用户的角度是从1开始数
        begin = line.find(key, begin+1)   # 从下一个位置继续查找

    return pos


#================在文件中查找==================
#此函数主用于将文件以行数为索引的key,关键字在行的位置作为value作为字典类型,调用pos_in_line函数处理，将字典返回给search_files函数。

def search_in_file(file_name, key):
    f = open(file_name,encoding='gbk',errors='ignore')        #打开文本文件
    count = 0                # 记录行数
    key_dict = dict()      # 定义字典，用户存放key所在具体行数对应具体位置
    
    for each_line in f:           #遍历文本文件中的每一行
        count += 1             #行数记录
        if key in each_line:  #如果关键字在某一行中
            pos = pos_in_line(each_line, key)  # key在每行对应的位置  调用pos_in_line函数 传入这个行和关键字
            key_dict[count] = pos
    
    f.close()
    return key_dict


#================主程序（在目录中查找）==================
#此函数主用于遍历当前目录下可以打开的txt文档,然后调用search_in_file函数进行处理。


def search_files(key, detail):    #第一步调用search_file函数 把 key, detail 参数传入进去
    all_files = os.walk(os.getcwd())  #遍历当前目录下的所有文档，返回一个三目元祖(0.目录，1.包含路径，2.包含文件)，将返回的结果赋值给all_files
    txt_files = []   #定义列表txt_files 

    for i in all_files:   #遍历all_files  注意这里的i为单次遍历的三元组，也就是说，这里的i是包含目录、路径和文件的三元组。
        for each_file in i[2]:  #遍历三元组的第三个值，即遍历文件，这里的each_file为单次遍历的文件
            if os.path.splitext(each_file)[1] == '.txt': # 根据后缀判断是否文本文件
                each_file = os.path.join(i[0], each_file)  #如果each_file 是文本文件  则将该文件的路径名称以及文件名称合并,并赋值给each_file 
                txt_files.append(each_file)  #列表txt_files 中追加each_file 此时的each_file为全路径含文件名 列表中追加的文本文件全路径

    for each_txt_file in txt_files:  #在列表txt_file中 遍历所有的文本文件 each_txt_file为单次遍历的文本文件名
        key_dict = search_in_file(each_txt_file, key)  #调用seach_in_file函数，传入单次遍历的文本文件名each_txt_file和用户输入的关键字key
        if key_dict:
            print('================================================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))
            if detail in ['YES', 'Yes', 'yes']:
                print_pos(key_dict)

key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')   #接受用户输入的关键字 key为用户输入的结果
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)  #请示用户是否打印  detail为请示结果
search_files(key, detail)  #调用函数search_files 传入关键字 key, detail 
