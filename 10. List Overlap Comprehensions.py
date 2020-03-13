a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(set([x for x in a for y in b if x==y]))


import random

p=random.sample(range(100),20)
q=random.sample(range(200),40)

print(set([x for x in p for y in q if x==y]))

result=[i for i in set(a) for j in b if i==j]
print(result)

print(i for i in set(a) if i in b)