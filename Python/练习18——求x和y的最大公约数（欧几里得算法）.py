def gcd(x, y):
    
    while y: 
        t = x % y 
        x = y 
        y = t 

    return x

x = int(input('请输入第一个数x:'))
y = int(input('请输入第二个数y:'))
print(gcd(x, y))

