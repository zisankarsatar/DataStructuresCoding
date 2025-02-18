def factorial(n):
    print(n)
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
result = factorial(25)
print(result)

def summation(n):
    print(n)
    
    if n == 0:
        return 0
    else:
        return n + summation(n-1)
    

result2 = summation(25)
print(result2)