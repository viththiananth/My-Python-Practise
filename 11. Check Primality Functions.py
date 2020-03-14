#Ask the user for a number and determine whether the number
# is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to
# help you. Take this opportunity to practice using functions,
# described below.

num=int(input("Please type the Number you want to calculate :"))
list1=[]

#Solution 1
def prime_num(num):
#    if num==1:

    for i in range(2,num):
        if num%i==0:
            list1.append(i)
    if list1==[]:
        print("This is a Prime Number")
    else:
        print("This is not a Prime Number")

a=prime_num(num)


#Solution 2
list2=[a for a in range(2,num) if num%a==0]
print(list2)

def check_prime(new_list):
    if num==1:
        print("Print Value other than 1")
    elif num==2:
        print("This is a Prime Number")
    elif list2==[]:
        print("This is a Prime Number")
    else:
        print("This is not a Prime Number")

a=check_prime(list2)