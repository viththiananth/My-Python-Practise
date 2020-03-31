while True:
    try :
        input_num = int(input("Please Guess the 4 Digit Number >>> "))
        if input_num in range(1000,10000):
            break
        else:
            print("Number is in out of range, Please try again")
    except:
        print("Thats not an Number")