def Bin(n):
    temp = ''
    if n:
        temp = Bin(n//2)
        temp += str(n%2)
        return temp
    else:
        return temp        

num = int(input('请输入一个十进制数：'))
print(num,'-->',Bin(num))
