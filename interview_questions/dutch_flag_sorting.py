"""
Dutch National Flag Sorting Problem
•⁠  ⁠For this problem, your goal is to sort an array of 0, 1 and 2's but you must do this in place, in 
linear time and without any extra space (such as creating an extra array). This is called the Dutch national 
flag sorting problem. For example, if the input array is (2,0,0.1,2.1] then your program should output 
(0.0.1,1,2,2) and the algorithm should run in O(n) time.
"""
def swap(arr, i1, i2):
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp
   
def natflag(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    
    while mid <= high:
        if arr[mid] == 0:
            swap(arr,low, mid)
            low += 1
            mid +=1
        elif arr[mid] == 2:
            swap(arr, mid, high)
            high -= 1
        else:
            mid += 1
    
    return arr 

print(natflag([2,1,0,2,1,1,0,0,2]))