import  random

wards = [[],[],[]]
a = 1
patients = [1,2,3,4,5,6,7]
while a==1:
    for patient in patients:
        index = random.randint(0,2)
        wards[index].append(patient)
        n0 = len(wards[0])
        n1 = len(wards[1])
        n2 = len(wards[2])
    if n0!=0 and n1!=0 and n2!=0:break
i = 1
for ward in wards:
    num = len(ward)
    print("%d号病房有%d位病人"%(i,num))
    print(ward)
    i += 1