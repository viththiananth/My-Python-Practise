import random

num=random.randint(1,9)
print(num)

guess=0
count=1

while guess!=num and guess!='exit':
    guess=input("Guess the Number between 1 and 9")

    if guess=='exit':
        break

#    while not type(guess)==int:
#        try:
#            guess==int(guess)
#        except ValueError:
#            guess=input('Enter Integer Value from 1 to 9')

    guess=int(guess)

    if guess>num:
        print("Too High")
        count+=1
    if guess<num:
        print("Too Low")
        count += 1
    if guess==num:
        print("Right Guess on",count,"Attempt")