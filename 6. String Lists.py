text: str=input('Please Input the Text: ')

#Using Slicing Method :
rvs_text=text[::-1]
print(text)
print(rvs_text)

if text==rvs_text:
    print("This Word is palindrome ")
else :
    print("This is normal word")


#Using Loops Method :
def reversed_word(word):
    x=''
    for i in range(len(word)):
