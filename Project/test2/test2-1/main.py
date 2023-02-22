numcount = 0
lettercount = 0
n = input("请输入待检查的语句：")
for i in n:
    if i.isdigit():
        numcount += 1
    if i.isalpha():
        lettercount += 1
print("此语句中字母有:%d个，数字有:%d个"%(lettercount,numcount))