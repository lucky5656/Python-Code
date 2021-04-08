#实现一个用于登记用户账号信息的界面（如果是带*号的是必填项，要求一定要有输入并且不能是空格）
import easygui as g
msg = '【*真实姓名为必填项】\n【*手机号码为必填项】\n【*E-mail为必填项】'
title = "账号中心"
fieldNames = ["用户名", "*真实姓名", "固定电话", "*手机号码", "QQ","*E-mail"]
fieldValues = []  # we start with blanks for the values
fieldValues = g.multenterbox(msg, title, fieldNames)

# 确保必填项字段不为空
while 1:
    if fieldValues == None:
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip()#当输入中有空格的时候，把头和尾的空格去掉#
        if fieldValues[i].strip() == "" and option[0] == '*':
            errmsg += ('"%s" 是必填字段.\n\n' % fieldNames[i])
    if errmsg == "":
        break  # no problems found
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

print("用户资料如下：%s" % str(fieldValues))
