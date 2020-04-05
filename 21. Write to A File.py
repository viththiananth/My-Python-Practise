#f=open("New File.txt",'a')
#f.write("\n New Text Added")
#f.close()
#
#f=open('New File.txt','r')
#print(f.read())
#

#p=open('New File1.txt','w')
#p.write("This is Viththi")
#p.close()
#
#p=open("New File1.txt",'r')
#print(p.read())

import os
if os.path.exists("New Test.txt"):
    os.remove("New Test.txt")
else:
    print("The File doesnot exist")

