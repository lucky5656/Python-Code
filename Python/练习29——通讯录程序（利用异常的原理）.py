#使用条件语句的代码非常直观明了，但是效率不高。
#因为程序会两次访问字典的键，一次判断是否存在（if name in contacts），一次获得值（例如：print(name + ' : ' + contacts[name]）。
#如果利用异常解决方案，我们可以简单避开每次需要使用in判断是否key存在字典中的操作。
#因为只要当key不存在字典中时，会触发KeyError异常，利用此特性我们可以修改代码如下：

print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

contacts = dict()

while 1:
    instr = int(input('\n请输入相关的指令代码：'))

    if instr == 1:
        name = input('请输入联系人姓名：')
        try:
            print(name + ' : ' + contacts[name])
        except KeyError:
            print('您输入的姓名不再通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        try:
            contacts[name] 
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            print(name + ' : ' + contacts[name])
            if input('是否修改用户资料（YES/NO）：') == 'YES':
                contacts[name] = input('请输入用户联系电话：')
        except KeyError:
            contacts[name] = input('请输入用户联系电话：')

    if instr == 3:
        name = input('请输入联系人姓名：')
        try:
            del(contacts[name]) # 也可以使用dict.pop()
        except KeyError:
            print('您输入的联系人不存在。')

    if instr == 4:
        break

print('|--- 感谢使用通讯录程序 ---|')
