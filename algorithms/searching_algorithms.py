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


#print(binarySearch([2,6,8,78,84,543,643], 543))
    
    
import math

def jumpSearch(list, key):
    n = len(list)
    step = math.sqrt(n)
    
    prev = 0
    
    while list[int(min(step, n)-1)] < key:
        prev = step
        step += math.sqrt(n)
        
        if prev >= n:
            return -1
    
    while list[int(prev)] < key:
        prev += 1
        
        if prev == min(step, n):
            return -1
        
    if list[int(prev)] == key:
        return int(prev)
    
    return -1

#print(jumpSearch([2,6,8,78,84,543,643], 78))

def rec_binary_search(list, key):
    #binary search with recursive
    
    #base case
    if len(list) == 0:
        return False
    
    #recursive case
    else:
        mid = int(len(list)/2)
        
        #if match found (base)
        if list[mid] == key:
            return True
        else:
            # lower
            if key < list[mid]:
                return rec_binary_search(list[:mid], key)
            # upper
            else:
                return rec_binary_search(list[mid+1:], key)
            
    return False

#have to fix            
print(rec_binary_search([2,6,8,78,84,543,643], 6545))