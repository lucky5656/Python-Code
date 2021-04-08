#写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。举例：get_digits(12345) ==>[1, 2, 3, 4, 5]
#解题思路：利用除以10取余数的方式，每次调用get_digits(n//10)，并将余数存放到列表中即可。要注意的是结束条件设置正确。

def get_digits(n):
    result = ''
    if n:
        result = get_digits(n//10)
        result += str(n%10)
    return list(result)

num = int(input('请输入一个数：'))
print(get_digits(num))
