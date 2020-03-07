name=input("Please Input your name")
age=int(input("Please Input your Age"))

print("Your Name is {} and age is {}".format(name,age))

import datetime
now = datetime.datetime.now()
x= now.year

x=x+(100-age)

count=int(input("Please Type How many times you want to print this?"))
for i in range(count):
    print("\nYou will be age of 100 @ the year of {}".format(x))