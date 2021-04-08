def Narcissus():
    for each in range(100,1000):
        temp = each
        sum = 0
        while temp:
            sum = sum + (temp%10) ** 3
            temp = temp // 10  #这里用地搬除

        if sum == each:
            print(each,end='\t')

print("所有的水仙花数分别是：",end ='')
Narcissus()
