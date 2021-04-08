def Huiwen(temp,start,end):
    if start > end:
        return 1
    else:
        if temp[start]==temp[end]:
            return Huiwen(temp,start+1,end-1)
        else:
            0

temp = input('请输入一段文字：')
length = len(temp)
end = len(temp)-1
if Huiwen(temp,0,end):
    if temp[0:length//2] == temp[length//2:length]:
        print('%s不是一个回文字符串！'%temp)
    else:
        print('%s是一个回文字符串！'%temp)
else:
    print('%s不是一个回文字符串！'%temp)
