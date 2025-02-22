def bubble_sort(arr):
    
    for i in range(len(arr)-1,0,-1): #azalarak tum listeyi gezmek
        for n in range(i): #liste icindeki elemanlari gexmek
            if arr[n] > arr[n+1]:
                temp = arr[n]
                arr[n] = arr[n+1]
                arr[n+1] = temp
                
    return arr

#print(bubble_sort([2,1,56,7,89,6,45,99,134]))

def merge_sorting(arr):
    if len(arr) > 1:
        mid = int(len(arr)/2)
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        
        merge_sorting(lefthalf)
        merge_sorting(righthalf)
        
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1
        
        while i < len(lefthalf):
            arr[k] = lefthalf[i] 
            i += 1
            k += 1
        
        while j < len(righthalf):
            arr[k] = righthalf[j] 
            j += 1
            k += 1
        
    return arr

#print(merge_sorting([12,7,8,6,1]))

def insert_sorting(arr):
    
    for i in range(1, len(arr)):
        
        current_value = arr[i]
        position = i
        
        #sublist
        while position > 0 and arr[position-1] > current_value:
            arr[position] = arr[position-1]
            position -= 1
        arr[position] = current_value
    
    return arr

#print(insert_sorting([12,7,8,6,1]))
               
def selection_sorting(arr):
    for i in range(len(arr)-1, 0, -1):
        positionOfMax = 0
        
        for location in range(1, i+1):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location
            
            temp = arr[i]
            arr[i] = arr[positionOfMax]
            arr[positionOfMax] = temp
            
    
    return arr

#print(selection_sorting([12,7,8,6,1]))

def selection_sorting_by_incrase(arr):
    for i in range(len(arr)):
        positionOfMax = 0
        
        for location in range(1, i+1):
            if arr[location] > arr[positionOfMax]:
                positionOfMax = location
            temp = arr[i]
            arr[i] = arr[positionOfMax]
            arr[positionOfMax] = temp
    return arr

print(selection_sorting_by_incrase([12,7,8,6,1]))
