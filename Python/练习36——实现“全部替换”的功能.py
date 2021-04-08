def file_replace(file_name,rep_word,new_word):
    f_read = open(file_name)

    content = []# 创建空的列表,用来存储数据
    count = 0# 设置需要改的字符串的的个数(初始值为0)

    for eachline in f_read:
        if rep_word in eachline:# 判断需要改的字符串或单词是否在这一行中
            count1 = eachline.count(rep_word) # 每行中需要改的字符串的个数
            eachline = eachline.replace(rep_word,new_word) # 改字符串
            count += count1  # 自加每行的个数
        content.append(eachline) # 加到列表中去

    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' %(file_name,count,rep_word,rep_word,new_word))

    if decide in ['YES','Yes','yes']:# 如果用户输入包含有这些字符,则重写文件的内容
        f_write = open(file_name,'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()

file_name = input('请输入文件名（E:\python\my codes\一个例子\newfile.txt）：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name,rep_word,new_word)
