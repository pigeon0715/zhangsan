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
'''

for i in range(10):
    print(i)
