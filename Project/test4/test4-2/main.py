class Dictclass(object):
    def __init__(self,dict):
        self.dict = dict
    def del_dict(self,key):
        if key in self.dict.keys():
            del self.dict[key]
            return self.dict
        else:
            return 'no result'
    def get_dict(self,key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return 'not found'
    def get_key(self):
        return self.dict.keys()
    def update_dict(self,dict2):
        self.dict.update(dict2)
        return self.dict
dict1={'1':'1','2':2,'3':3}
a = Dictclass(dict1)
e = 1
while e==1:
    print('1：删除 2：查找 3：合并 4：返回键值 5:结束程序')
    i = int(input('请输入操作数：'))
    if i==1:
        s = str(input('请输入需要删除的对象：'))
        print(a.del_dict(s))
    elif i==2:
        c = str(input('请输入需要查找的对象：'))
        print(a.get_dict(c))
    elif i==3:
        d = str(input('请输入键：'))
        f = int(input('请输入值：'))
        dict2 = {d:f}
        print(a.update_dict(dict2))
    elif i==4:
        print(a.get_key())
    else:
        e = 2