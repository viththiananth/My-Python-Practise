#Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
#Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

#Solution 1
import random
import string

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

print("".join(random.sample(s,20)))

#Solution 2
import random
import string

def password_gen(size,char=string.ascii_letters+string.digits+string.punctuation):
    return ''.join(random.choice(char) for i in range(size))

a=password_gen(int(input("Please type length of the Password")))
print(a)


#Solution 3
import random
import string

def password_gen1(size=12, char=string.ascii_letters+string.punctuation+string.digits):
    lst1=[]
    for i in range(size):
        lst1.append(random.choice(char))
    return ''.join(lst1)

c=password_gen1(15)
print(c)