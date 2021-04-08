def Dec2Bin(dec): 
    temp = [] 
    result = '' 

    while dec: 
        quo = dec % 2 
        dec = dec // 2 
        temp.append(quo) 

    while temp: 
        result += str(temp.pop()) 

    return result 

x = int(input('请输入一个十进制数：'))
print(Dec2Bin(x))
