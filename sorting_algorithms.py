def bubble_sort(arr):
    
    for i in range(len(arr)-1,0,-1): #azalarak tum listeyi gezmek
        for n in range(i): #liste icindeki elemanlari gexmek
            if arr[n] > arr[n+1]:
                temp = arr[n]
                arr[n] = arr[n+1]
                arr[n+1] = temp
                
    return arr

print(bubble_sort([2,1,56,7,89,6,45,99,134]))