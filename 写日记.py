import time
now = time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入今天的心情：")
with open("日记.txt","a",encoding="utf8") as f:
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("——————————————"+"\n")

# \t 空格
# \n 换行