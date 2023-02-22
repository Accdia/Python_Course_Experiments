def myfunc(xlist):#定义函数
    num = 0#初始化变量
    for i in xlist:#求和
        num += i
    c = num / len(xlist)#求平均值
    upavg = []#创建空列表
    for k in xlist:#放入大于平均值的数
        if k>c:
            upavg.append(k)
    res = (c,upavg)#组合
    return res
x = input()#从键盘输入
xlist=x.split(",")#以逗号分隔
xlist = [float(xlist[i]) for i in range(len(xlist))]#将每个值转换为float型
print(myfunc(xlist))#输出结果