text=input('Please Input the Text: ')
rvs_text=text[::-1]
print(text)
print(rvs_text)

if text==rvs_text:
    print("This Word is palindrome ")
else :
    print("This is normal word")