def findStr(desStr,subStr):
    count = 0
    length = len(desStr)
    if subStr not in desStr:
        print("在目标字符串中未找到字符串！")
    else:
        for each1 in range(length - 1):#因为你找的是长度2的字符串，所以length减了1
            if desStr[each1] == subStr[0]:
                if desStr[each1+1] == subStr[1]:
                    count += 1

        print('字符串在目标字符串中共出 %d 次' % count)

desStr = input('请输入目标字符串：')
subStr = input('请输入子字符串（两个字符）：')
findStr(desStr,subStr)

#字符串这里是用索引查找的，例如a='abc'长度是3，索引是从0开始，
#单个字母索引最大就是a[2]而不是a[3]
#而这里的逻辑是第一个字母和带查找的双字母字符串的首字母对上了，再看下一个字母和剩余的是否对上
#        for each1 in range(length-1):      
#            if desStr[each1] == subStr[0]:
#                if desStr[each1+1] == subStr[1]:
#                    count += 1
#因为第二个字母desStr[each1+1]能取到最大索引，这里desStr[each1]是判断的双字母字符串首字母，能取到的索引又减了1
