class Students:
    def __init__(self,name,age,score1,score2,score3):
        self.name = name
        self.age = age
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    def get_name(self):
        return str(self.name)
    def get_age(self):
        return int(self.age)
    def get_score(self):
        num = [self.score1,self.score2,self.score3]
        z=max(num)
        return int(z)
s1 = Students("A","12","1","2","3")
s2 = Students("B","13","4","5","6")
print(s1.name)
print(s2.get_score())
print(s2.get_age())