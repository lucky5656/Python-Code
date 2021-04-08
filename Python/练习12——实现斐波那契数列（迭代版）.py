def fab(n):
    a1 = 1
    a2 = 1
    a3 = 1
    if n < 1:
        print("输入有误！")
        return -1
    while (n-2) > 0:
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        n -= 1
    return a3

n=int(input("请输入经过的月份："))
result = fab(n)
if result != -1:
    print('总共有%d对小兔子诞生！'% result)
