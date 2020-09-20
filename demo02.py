#判断  缩进
'''
a = 1
b = 2
if a > b:
    print("a比b大")
else:
    print("b更大")
'''

'''
age = int(input("请输入你的年龄："))
if age > 60:
    print("你应该退休了")
elif age > 30:
    print("中年危机")
elif age > 18:
    print("今天不学习，明天找不到工作")
else:
    print("图样图森破")
'''

'''
a = True
if type(a) is int:
    print("是数字")
elif type(a) is str:
    print("是字符串")
else:
    print("其他")
'''
'''
a = 1
while a < 10:
    print("hhhhh",a)
    a = a + 1
'''
'''
#遍历
#a = "今天，你吃了吗？"
a = ["张三","李四","王麻子","暖暖","洛昂","墨丘利","洛洛梨","池小鱼","王红花","左一"]
for i in a:
    print(i)

b = list(range(0,100,5)) #自动生成了一个数列,步进/步长
print(b)
for i in b:
    print(i)

for i in range(10):
    if i == 4:
        break
    print(i)

'''
#第三次课
'''
def checkname(username):
    if len(username) >= 5 and len(username) <= 8:
        if username[0] in "qwertyuiopasdfghjklzxcvbnm":
            print("ok")
        else:
            print("账号首字母必须为小写")
    else:
        print("账号长度是5—8位") 

checkname("3213132swwwwr")
#def 方法的声明
#checkname 方法的名字
#usernam 方法的参数


def jiafa(a,b):
    if type(a) is int and type(b) is int:
        print(a+b)
    else:
        print("输入的参数不正确")

jiafa("12",40)

'''
#把print换成return，则可以把retur的值用于后续代码中

#异常捕获
try:
    print(2+ajshf)
except Exception as e:
    print("代码写错了",e)