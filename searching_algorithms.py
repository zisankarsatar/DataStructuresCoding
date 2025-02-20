def sequentialSearchUnorderedList(list, key):
    index = 0
    found = False
    
    while index < len(list) and not found:
        if list[index] == key:
            found = True
        else:
            index +=1
            
    return(found,index)
            
#print(sequentialSearchUnorderedList([2,6,3,1,8,78,8,43,54,34], 34))

def sequentialSearchOrderedList(list, key):
    index = 0
    found = False
    stop = False
    
    while index < len(list) and not found and not stop:
        if list[index] == key:
            found = True
        else :
            if key < list[index]:
                stop = True
            else :
                index += 1
                
    return (index, found)

#print('index, found : ')
#print(sequentialSearchOrderedList([2,6,8,78,843,543,643], 34))

def binarySearch(list, key):
    first_index = 0
    last_index = len(list) - 1
    
    found = False
    
    while first_index <= last_index and not found:
        
        middle_index = int((first_index + last_index)/2)
        
        if list[middle_index] == key:
            found = True
        else:
            if key < list[middle_index]:
                last_index = middle_index - 1
                print('lower half')
            else:
                first_index = middle_index + 1
                print('upper half')
                    
    return found


print(binarySearch([2,6,8,78,84,543,643], 543))
    