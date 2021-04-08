#先定义一个温度类，再定义两个描述符类用于描述摄氏度和华氏度两个属性，两个属性会自动转化。

class Celsius:
    def __init__(self,value = 26.0):
        self.value = float(value)

    def __get__(self,instance,owner):
        return self.value

    def __set__(self,instance,value):
        self.value = float(value)

class Fahrenheit:
    def __get__(self,instance,owner):
        return instance.cel * 1.8 + 32

    def __set__(self,instance,value):
        instance.cel = (float(value) - 32) / 1.8
        
class Temperature:
    cel = Celsius()
    fah = Fahrenheit()
