def find(ordered_list,element_to_find):
    start_index=1
    end_index=len(ordered_list)-1

    while True:
        middle_index=(end_index-start_index)/2
            
        if middle_index < start_index or middle_index > end_index or middle_index < 0:
            return False

        middle_element=ordered_list[int(middle_index)]
        if middle_element==element_to_find:
            return True
        elif middle_element<element_to_find:
            start_index=middle_index
        else:
            end_index=middle_index

if __name__ == "__main__":
    l=[1,2,3,4,5,6,7,8,9]
    print(find(l,8))