Name_Counter ={}
with open('file_to_save.txt','r') as f:
    line=f.readline()

    while line:
        line=line.strip()
        for line in Name_Counter:
            Name_Counter[line]+=1
        else:
            Name_Counter[line]=1
        line=f.readline()

print(Name_Counter)