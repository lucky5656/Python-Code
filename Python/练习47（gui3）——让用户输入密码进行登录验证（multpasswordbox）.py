from easygui import *
msg = "验证登陆信息"
title = "密码函数multpasswordbox示例"
fieldNames = ["服务器 ID", "用户 ID", "密码"]
fieldValues = []  # we start with blanks for the values
fieldValues = multpasswordbox(msg, title, fieldNames)
print("输入的信息是: %s" % str(fieldValues))
