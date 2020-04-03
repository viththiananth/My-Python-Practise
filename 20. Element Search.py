# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

def check_num(list1,num):
    for i in list1:
        if i==num:
            return True
    return False

if __name__=="__main__":
    l=[1,2,3,4,5,6,7,8,9,10]
    check_num([1,2,3,4,5,6,7,8,9,10],4)
    print(check_num(l,2))
    print(check_num(l,122))
    print(check_num(l,10))
    print(check_num(l,-1))