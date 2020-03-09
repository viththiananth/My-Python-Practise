a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lst=[]
for x in a:
    for y in b:
        if x==y:
            lst.append(x)
print(set(lst))



import random
a1=random.sample(range(0,30),k=20)
a2=random.sample(range(0,20),k=12)
print(a1)
print(a2)
lst_overlap=[]
for x in a1:
    for y in a2:
        if x==y:
            lst_overlap.append(x)
print(set(lst_overlap))