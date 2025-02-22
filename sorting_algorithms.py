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

print(merge_sorting([12,7,8,6,1]))
               