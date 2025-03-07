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
    """
    dynamic programing ile fibonachi cozumu
    """
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
    
#print(dynamic_fibo(3))
    
#recursive
def recursive_catalan(n):
    """
    recusrive solution for catalan numbers
    """
    #base case
    if n <= 1:
        return 1
    
    res = 0 
    
    for i in range(n):
        res += recursive_catalan(i) * recursive_catalan(n-i-1)
        
    return res

#for i in range(10):
#    print(recursive_catalan(i))
    
def dynamic_calatan(n):
    """
    dynamic progpraming solution to catalan problem
    """
    #base case
    if n <= 1:
        return 1
    
    #depola
    catalan = [0 for i in range(n+1)]
    
    # ilk iki degeri doldur
    catalan[0], catalan[1] = 1,1
    
    #listeyi doldur
    for i in range(2, n+1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j]*catalan[i-j-1]
            
    return catalan[n]
    
for i in range(5):
    print(dynamic_calatan(i))