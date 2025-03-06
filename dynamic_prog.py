def recur_fibo(n):
    """
    recursive func with fibonachi 
    """
    
    #base case
    if n <= 1:
        return n
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2)) 

#print(recur_fibo(9))

#                                           recur_fibo(9)
#                      recur_fibo(8) +                     recur_fibo(7)
#           recur_fibo(7) + recur_fibo(6)    +         recur_fibo(6) + recur_fibo(5)
# ....

def dynamic_fibo(n):
    fibo_list = [0,1]
    
    while len(fibo_list) < n+1:
        fibo_list.append(0)
        
    #base_case
    if n <= 1:
        return n
    else:
        if fibo_list[n-1] == 0:
            fibo_list[n-1] = dynamic_fibo(n-1)
        if fibo_list[n-2] == 0:
            fibo_list[n-2] = dynamic_fibo(n-2)
            
        fibo_list[n] = fibo_list[n-2] + fibo_list[n-1]
    
    return fibo_list[n]
    
print(dynamic_fibo(3))
    