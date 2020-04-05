##Option 1 : Direct method
list1 =[]
path1 = 'E:\\Temp\\Compare_Text Files\\One_Prime Numbers.txt'
with open(path1, 'r') as f1:
    num1=f1.readline()
    while num1:
        num1=num1.strip()
        list1.append(num1)
        num1=f1.readline()

int_list1=[int(i) for i in list1]
#print(int_list1)

list2=[]
path2 = 'E:\\Temp\\Compare_Text Files\\Other_Happy Numbers.txt'
with open(path2, 'r') as f2:
    num2=f2.readline()
    while num2:
        num2=num2.strip()
        list2.append(num2)
        num2=f2.readline()

int_list2=[int(i) for i in list2]

#Now Lets compare the 2 lists for common Integers
#Option1
common_list=[x for x in int_list1 if x in int_list2]
print(common_list)

#Option 2
common_list1 = []
for i in int_list1:
    for j in int_list2:
        if i==j:
            common_list1.append(i)





#Option 2: Using Function
def int_list(list_name):
    list2=[]
    with open(list_name,'r') as f:
        str_line=f.readline()
        while str_line:
            str_line=str_line.strip()
            list1.append(str_line)
            str_line=f.readline()
    
    int_list1=(int(i) for i in list1)
    return(int_list1)

a=int_list('E:\\Temp\\Compare_Text Files\\One_Prime Numbers.txt')
b=int_list('E:\\Temp\\Compare_Text Files\\Other_Happy Numbers.txt')

overlap_list=[x for x in a if x in b]
print(overlap_list)