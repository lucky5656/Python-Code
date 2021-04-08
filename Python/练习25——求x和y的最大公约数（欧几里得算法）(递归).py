def gcd(x,y):  
    if y == 0:  
        return x  
    else:  
        return gcd(y,x%y)
    
x = int(input('请输入第一个数x:'))
y = int(input('请输入第二个数y:'))
print(gcd(x, y))
