a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b=list(map(lambda x : x%2==0,a))
print(b)


even_number=[num for num in a if num%2==0]
print(even_number)