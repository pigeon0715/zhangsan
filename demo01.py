'''
print("hello,world!") # 字符串
print(2333) # 整数
print(2.333) # 小数
print(True) # 布尔值 true false
print(()) # 元组
print([]) # 数组
print({}) # 字典
print("哈哈"*10)
print("哈哈"+"嘻嘻") #字符串的拼接
print("哈哈","嘻嘻")
print(1+1)
print(2>3)

a=input("请输入：")
print("input获取的内容：",a)

print(type("hello,world!"))
print(type(2333)) 
print(type(2.333)) 
print(type(True)) 
print(type(()))
print(type([])) 
print(type({}))


a=str(2333)
print(type(a))

a = float(input("请输入："))
b = float(input("请输入："))
print("a+b=",a+b)

'''

'''
#元组，下标，从0开始编号
a =(1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False)
print(a[-1])
#切片
print(a[0:4]) #左闭右开,开头的下标（0）和最后一个下标可省略
print(a[4:9])
print(a[9:])
#print(a.index("嘻嘻"))
#print(a.count("哈哈"))

#二维元组
b=(a,"hh","xx")
print(b[0][2])
'''

#元组写好后不能修改数据，数组可修改
"""
a =[1,2,3,4,"哈哈","嘻嘻",True,False]
a.append("测试")
print(a)
a.insert(0,"0代表插入位置的下标")
print(a)
a.pop(5) #剪切
print(a)
b = a.pop(1)
c = a.pop(1)
print(b+c)
# a.clear()  清空
xx=["你好","不好"]
a.extend(xx)
print(a)
a.remove("你好")
print(a)

xx = [0,False,1,True]
a = xx.count(0)
print(a)
"""

'''
a={"name":"张三",0:"haha","age":25}
#取值
print(a["name"])
b = a.get("name")
print(b)
#新增
a["height"]="183cm"
print(a)
#修改
a["name"] = "李四"
print(a)
#剪切
b=a.pop("name")
print(b)
print(a)

'''


a=[]
print(a.count("hh"))