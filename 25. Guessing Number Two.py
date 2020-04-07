list1=[i for i in range(0,101)]
my_num=int(input("Please Input the Number to be find : "))
guess_count=0

while len(list1)>3:
    middle_index=int((len(list1)-1)/2)
    guess_num=list1[int((len(list1)-1)/2)]
    print("Guessed Number is : ",guess_num)

    x=input("Whether this number Number greater('H')/less('L')/correct('C') than defined Number?".format(guess_num))

    if x=="h":
        list1=list1[middle_index:(len(list1))]
        print(list1)
        guess_count+=1

    elif x=="l":
        list1=list1[0:middle_index]
        print(list1)
        guess_count+=1
    
    elif x=="c":
        guess_count+=1
        print("Yes. You found the correct Number {}\nGuess Count is : {}".format(my_num,guess_count))
        break
    
    else:
        for i in list1[1:]:
            print("XXX_Guessed Number is : ",i)
            x=input("XXX_Whether this number Number greater('H')/less('L')/correct('C')?".format(i))
            if x=='h' or x=='l':
                guess_count+=1
            elif x=='c':
                guess_count+=1
                print("Yes. You found the correct Number {} @ the guess count of {}".format(my_num,guess_count))
                break