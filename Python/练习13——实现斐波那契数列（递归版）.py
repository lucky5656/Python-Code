def fab(n):
    if n < 1:
        print("输入有误！")
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

n=int(input("请输入经过的月份："))
result = fab(n)
if result != -1:
    print('总共有%d对小兔子诞生！'% result)
