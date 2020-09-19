'''
# 通过代码获取两段内容，并计算他们长度的和。
a = input("请输入：")
b = input("请输入：")
print("两段字符的长度=",len(a)+len(b))

#练习：获取用户输入的个人信息（name，age，sex）并储存到字典中。
name = input("请输入姓名：")
age = input("请输入年龄：")
sex = input("请输入性别：")
userinfo={"name":name,"age":age,"sex":sex}
print(userinfo)

#现在有10个学生的成绩，需要录入到系统中，这十个人分别是：
#"张三","李四","王麻子","暖暖","洛昂","墨丘利","洛洛梨","池小鱼","王红花","左一"
#并且名字和成绩需要对应上，且大于60和小于60的需要分开存放。

highgrade = {}  #定义了一个空字典，用于储存大于60的信息
lowgrade = {}
studenlist=["张三","李四","王麻子","暖暖","洛昂","墨丘利","洛洛梨","池小鱼","王红花","左一"]
a = 0 #定义了一个变量，用于控制下标变化
while a < len(studenlist):
    grade=int(input("请输入"+studenlist[a]+"的成绩：")) #注意转换格式
    if grade < 60 :
        lowgrade[studenlist[a]] = grade #字典的新增
    else:
        highgrade[studenlist[a]] = grade
    a = a + 1
print("小于60分：",lowgrade)
print("大于60分：",highgrade)


highgrade = {}  #定义了一个空字典，用于储存大于60的信息
lowgrade = {}
studenlist=["张三","李四","王麻子","暖暖","洛昂","墨丘利","洛洛梨","池小鱼","王红花","左一"]
for i in studenlist:
    grade=int(input("请输入"+i+"的成绩：")) #注意转换格式
    if grade < 60 :
        lowgrade[i] = grade #字典的新增
    else:
        highgrade[i] = grade
print("小于60分：",lowgrade)
print("大于60分：",highgrade)


#打印九九乘法口诀表。

for i in range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,"=",i*j,end=" ")
    print()

'''
'''
#用print打印模拟红绿灯的功能，红灯30次，绿灯35次，黄灯3次。
for i in range(0,30):
    print("红灯还有",30-i,"秒结束")
for j in range(35):
    print("绿灯还有",35-j,"秒结束")
for k in range(3):
    print("黄灯还有",3-k,"秒结束")


light = {"红灯":30,"绿灯":35,"黄灯":3}
while True: #死循环
    for i in light: #循环灯的颜色
        for j in range(light[i]): #循环时间
            print(i,"倒计时还有",light[i]-j,"秒")

'''

#用代码实现注册的功能。
#用户输入账号密码，要求账号长度是5—8位，密码6—12位，且账号必须小写开头。
#储存到字典中，{username：password}

userinfo={}
username=input("请输入账号：")
password=input("请输入密码：")
if len(username) >= 5 or len(username) <= 8:
    if username[0] in "qwertyuiopasdfghjklzxcvbnm":
        if len(password) >=6 and len(password) <=12:
            print("ok",{username:password})
        else:
            print("密码长度为6—12位")
    else:
        print("账号首字母必须为小写")
else:
    print("账号长度是5—8位") 

