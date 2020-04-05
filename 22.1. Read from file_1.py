counter_dict = {}

with open('Sun directory files.txt','r') as f:
    line=f.readline()
    print(line[3:-26])
    while line:
        line=line[3:-26]

        if line in counter_dict:
            counter_dict[line]+=1
        else:
            counter_dict[line]=1
        
        line=f.readline()

print (line)
print(counter_dict)