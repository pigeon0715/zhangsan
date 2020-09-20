'''
import time
for i in range(10):
    time.sleep(1)
    print(i)

import random
a = random.randint(0,100)
print(a)

'''
#class 声明类的名字。    类的名字首字母必须大写。   面向对象编程。
#类里面所有的方法，都必须要传一个参数，叫self。
'''
class Boyfriend():
    def __init__(self,sex,hight,weight,hair):
        self.sex = sex
        self.hight = hight
        self.weight = weight
        self.hair = hair
    def caiyi(self,num):
        print("你性别为"+self.sex+"身高"+self.hight+"体重"+self.weight+"的男朋友陆景和开始了他的才艺表演之")
        if num == 1:
            print("跳伞")
        elif num == 2:
            print("画油画")
        else:
            print("打游戏")
    def cook(self):
        print("精通八大菜系")
    def work(self):
        print("艺术家")

#类的实例化
lujinghe = Boyfriend("男","182cm","70kg","蓝发")
lujinghe.caiyi(1)
lujinghe.work()
print(lujinghe.hair)
'''

class Car():
    def __init__(self,brand,color,neishi,jilun):
        self.brand = brand
        self.color = color
        self.neishi = neishi
        self.jilun = jilun

    def fly(self):
        print("车子开始起飞")
    
    def a(self):
        print("test")

zhangsan = Car("宝马","彩虹色","豪华","独轮车")
zhangsan.fly()

class Che(Car):
    def a(self):
        print("类的重写")
    pass
#继承。 Car:父类，Che:子类。

yiliangche = Che("奔驰","樱色","豪华","4轮")
print(yiliangche.color)
yiliangche.a()