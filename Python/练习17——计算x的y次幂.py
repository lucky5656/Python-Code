def power(x,y): 
    result = 1 

    for i in range(y): 
        result *= x 

    return result

x = int(input('请输入底数x:'))
y = int(input('请输入指数y:'))
print(power(x,y))

