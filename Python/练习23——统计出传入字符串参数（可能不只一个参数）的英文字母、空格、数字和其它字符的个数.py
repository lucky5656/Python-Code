def count(*param):  
    length = len(param)  
    for i in range(length):  
        word = 0  
        num = 0  
        spa = 0  
        oth = 0  
        for j in param[i]:  
            if j.isalpha():  
                word += 1  
            elif j.isspace():  
                spa += 1  
            elif j.isdigit():  
                num += 1  
            else:  
                oth += 1  
        print ('第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个'%(i+1,word,num,spa,oth))

count('I love fish','I love you')
