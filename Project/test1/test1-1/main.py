i = 1#计数初值
password = 123456789#初始密码
while i < 4:#循环判断密码错误次数
    a = int(input("Please input password:"))
    if a==password:#判断
        print("The password is true")
        break
    else:#判断
        print("The password is false The number of errors is ",i)
        i +=1
    if i==4:
        print("The password is locked ")