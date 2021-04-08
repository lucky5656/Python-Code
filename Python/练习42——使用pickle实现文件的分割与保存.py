#编写一个程序，要求使用pickle将文件（newfile.txt）里的对话按照以下要求腌制成不同文件。
import pickle
def save_pickle_file(son,mom,count):
    file_name_son = 'son_' + str(count) + '.txt'
    file_name_mom = 'mom_' + str(count) + '.txt'
 
    son_pickle_file = open(file_name_son,'wb')
    mom_pickle_file = open(file_name_mom,'wb')
 
    pickle.dump(son,son_pickle_file)
    pickle.dump(mom,mom_pickle_file)
 
    son_pickle_file.close()
    mom_pickle_file.close()
 
def split_file(file_name):
    f = open(file_name)
    son = []
    mom = []
    count = 1
 
    for each_line in f:
        if each_line[:6] != '======':
            (role,line_spoken) = each_line.split('：',1)
            if role == '儿子':
                son.append(line_spoken)
            elif role == '妈妈':
                mom.append(line_spoken)
        else:
            save_pickle_file(son,mom,count)
            count += 1
            son = []
            mom = []
 
    save_pickle_file(son,mom,count)
 
    f.close()
 
split_file('newfile.txt')
