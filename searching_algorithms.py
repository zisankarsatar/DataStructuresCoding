def sequentialSearchUnorderedList(list, key):
    index = 0
    found = False
    
    while index < len(list) and not found:
        if list[index] == key:
            found = True
        else:
            index +=1
            
    return(found,index)
            
print(sequentialSearchUnorderedList([2,6,3,1,8,78,8,43,54,34], 34))