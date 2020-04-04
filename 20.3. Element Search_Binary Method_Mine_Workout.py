def find_number(list_number,num_to_check):
    Start_Index=0
    End_Index=len(list_number)-1
    new_list=list_number
    not_found=False

    while len(new_list)>2:
        middle_index=(End_Index-Start_Index)/2
        middle_Element=new_list[int(middle_index)]
        print("\nMiddle Index : ",middle_index)
        print("Start Element : ", new_list[0])
        print("End Element : ", new_list[End_Index-1])
        print("Middle Element : ",middle_Element)
        print("Element to Match : ",num_to_check, "\n")

    #If number is first or last
        if new_list[0]==num_to_check or new_list[-1]==num_to_check:
            print("Number in List")
            break

    #If number is in Second Half of the list
        elif middle_Element<num_to_check:
            Start_Index=middle_index
            new_list=new_list[int(Start_Index):int(End_Index+1)]
            print(new_list)
            End_Index=len(new_list)
            Start_Index=0
            print(End_Index)
            not_found=False
            
    #If number is in First Half of the list
        elif num_to_check<middle_Element:
            End_Index=middle_index
            new_list=new_list[int(Start_Index):int(End_Index+1)]
            print(new_list)
            End_Index=len(new_list)
            print(End_Index)
            not_found=False
            
    #If Number is match with the middle number
        else:
            not_found=True
            break

    if not_found:
        print("Number in List")
    else:
        print("Number not in List")

l1 = [10,22,43,56,65,79,88,92,102,566]
n1 = 93
find_number(l1,n1)
    