a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst=[]

check=int(input("Please Input the Number to check : "))
for i in a:
    if i<check:
        lst.append(i)
print(lst)