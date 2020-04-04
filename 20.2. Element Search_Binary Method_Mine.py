def find(list_of_number, number_to_identify):
    Start_Index =1
    End_Index=len(list_of_number)
    
    while True:
        new_list=[]
        Middle_Index=(End_Index-Start_Index)/2
        Middle_Element=list_of_number[int(Middle_Index)]
    
    if Middle_Element<number_to_identify:
        new_list=[list_of_number[Middle_Index]:list_of_number[End_Index]]
    else:
        End_Index=Middle_Index



list1=[1,2,3,4,5,6,7,8]
find(list1,2)