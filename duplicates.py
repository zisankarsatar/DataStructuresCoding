"""
Find All Duplicates in Array in Linear Time
•⁠  ⁠This is a common interview question where you need to write a program to find all duplicates in an array where the 
numbers in the array are in the range of O to n-1 where n is the size of the array. For example: [1, 2, 3, 3] is okay but 
[1, 2, 6, 3] is not. In this version of the challenge there can be multiple duplicate numbers as well.
"""

def duplicates(arr):
    dups =[]
    
    for i in range(0, len(arr)):
        #mutlak aliniyor
        if abs(arr[i]) == len(arr):
            el = -1
        else:
            el = arr[abs(arr[i])]
            
        if el > 0:
            #arr[abs(arr[i])] = -arr[abs(arr[i])]
            arr[abs(arr[i])] = -el
        elif el == 0:
            arr[abs(arr[i])] = -len(arr)
        else:
            if abs(arr[i]) == len(arr):
                dups.append(0)
            else:
                dups.append(abs(arr[i]))
                
    return dups

# eksi deger([1,2,1,4,-4,0]) degeri girildiginde cortluyor
# liste uzunlugu girildiginde [1,2,1,4,6,0] 0 olarak dump listesine ekliyor 6 degerini
print(duplicates([0,2,1,-4,6,0]))