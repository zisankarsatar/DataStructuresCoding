def factorial(n):
    #print(n)
    
    #base case
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
result = factorial(5)
print(result)

def summation(n):
    #print(n)
    
    #base case
    if n == 0:
        return 0
    else:
        return n + summation(n-1)
    

result2 = summation(5)
print(result2)

def stringReverse(word):
    
    #base_case
    if len(word) <= 1:
        return word
    
    #recursion
    return stringReverse(word[1:]) + word[0]

print(stringReverse('zisan'))

def multiply(x,y):
    #carpma
    
    #base_case
    if y == 1:
        return x
    
    #recursion
    return multiply(x,y-1) + x

print(multiply(3,3))

def power(a,b):
    #ussu
    
    if b == 0:
        return 1
    
    return multiply(a, power(a, b-1))

print(power(3,3))
