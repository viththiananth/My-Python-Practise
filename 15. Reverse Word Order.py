#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.


def rvs_string(word):
    lst_string=word.split()
    print(lst_string)
    reverse_string=lst_string[::-1]
    print(reverse_string)
    final_string= " ".join(reverse_string)
    print(final_string)


a=rvs_string("My Name is Viththi")
print (a)


def reverse_v2(x):
    y = x.split()
    return " ".join(y[::-1])

b=reverse_v2("Ma asd da")
print(b)