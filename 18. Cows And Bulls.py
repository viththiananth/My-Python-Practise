#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

def game_play(list1,list2):
    common_list=[i for i,j in zip(list1,list2) if i==j]
    print(len(common_list),"Cows, ",(4-len(common_list)),"Bulls")

def game_win(list1,list2):
    if list1==list2:
        return ("Game Over")
    else:
        return("Game need to continue")

if __name__=="__main__":
    print("Welcome to the Cows and Bulls Game")
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 Cows!")
    print("Type exit at any prompt to exit.")
    
    str_num2=str(random.randint(1000,9999))
    list2=[int(j) for j in str_num2]
    print(list2)
    guess=0
    input_num=0

#while guess!=num and guess!='exit':
#    guess=input("Guess the Number between 1 and 9 : ")
#
#    if guess=='exit':
#        break

    while True:
        while input_num not in range(1000,9999):
            input_num = input("Please Guess the 4 Digit Number : ")
        
        str_num1=str(input_num)
        list1=[int(i) for i in str(str_num1)]

        game_play(list1,list2)
        guess+=1
        game_win(list1,list2)
        if game_win(list1,list2)=="Game Over":
            print("Number of Guesses Tried : ", guess)
            break
