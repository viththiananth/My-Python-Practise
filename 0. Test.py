def select_num():
    user_num=0
    while int(user_num) not in range (1000,10000):
        user_num=int(input("Please Guess the 4 Digit Number >>>"))
    return user_num

select_num()