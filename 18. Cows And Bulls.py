#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random


str_num2=str(random.randint(1000,9999))
list2=[int(j) for j in str_num2]
print(list2)

input_num = input("Please Guess the 4 Digit Number : ")
str_num1=str(input_num)
list1=[int(i) for i in str(str_num1)]

common_list=[i for i,j in zip(list1,list2) if i==j]
print(len(common_list),"Cows, ",4-len(common_list),"Bull"))

#def compare_num(num,input_num)

#    print("Welcome to the Cows and Bulls Game")
#    print("Enter a Number on your Guess")
#    