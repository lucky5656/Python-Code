def power(x,y):
    if y == 0:
        result = 1
    else:
        result = x*power(x,y-1)
    return result

x = int(input('请输入底数x:'))
y = int(input('请输入指数y:'))
print(power(x,y))

#x = 2
#y = 3
#result = 2 * power(2,2)
#result = 2 * 2 * power(2,1)
#result = 2 * 2 * 2 * 1 = 8
