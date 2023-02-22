import random#映入随机数

i = 1#循环开启条件
print("开始猜拳 0代表石头 1代表剪刀 2代表布")#提示
while i == 1:
    key = random.randint(0, 2)#产生随机数
    a = int(input("请输入相应数字:"))#输入对应数字以判断
    if a == key:#罗列每种情况判断
        print("平局", key)
    elif a == 0 and key == 1:
        print("你赢了", key)
    elif a == 0 and key == 2:
        print("你输了", key)
    elif a == 1 and key == 0:
        print("你输了", key)
    elif a == 1 and key == 2:
        print("你赢了", key)
    elif a == 2 and key == 0:
        print("你赢了", key)
    else:
        print("你输了", key)
    i = int(input("输入：1开始下一局，输入其他数字结束程序:"))#结束程序条件
