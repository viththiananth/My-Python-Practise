list_of_number=[1,2,3,4,5,6,7]
number_to_identify=6

Start_Index=0
End_Index=len(list_of_number)
new_list=[]
middle_index=(End_Index-Start_Index)/2
middle_Element=list_of_number[int(middle_index)]

print(middle_index)
print(middle_Element)

#If number is in Second Half of the list

if middle_Element<number_to_identify:
    Start_Index=middle_index
    new_list=list_of_number[int(Start_Index):int(End_Index)]
    print(new_list)

#If number is in First Half of the list
elif number_to_identify<middle_Element:
    End_Index=middle_index
    new_list=list_of_number[int(Start_Index):int(End_Index)]
    print(new_list)

#If Number is match with the middle number
else:
    print("Number is available within the list")