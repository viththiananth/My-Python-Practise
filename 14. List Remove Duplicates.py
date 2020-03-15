#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

#Extras:

#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.




def unique_list(list1):
    a= set(list1)
    return a

def unique_list_loop(list1):
    y=[]
    for i in list1:
        if i not in y:
            y.append(i)
    return y

lst1=[1,2,2,2,2,4,5,5,5,6,6,7,8]

print(unique_list(lst1))
print(unique_list_loop(lst1))