"""
### Generate Primes Up To N Using Sieve of Eratosthenes Algorithm
•⁠  ⁠The sieve of Eratosthenes algorithm generates all the primes up to a given limit. 
This is a common and fast algorithe used to generate a list of primes up to a given limit. It works by making 
a list from 1 to N, and then iterating through the list and progressively removing non-prime, composite numbers 
until only primes are left in a list.
"""
def sieve(limit):
    bools = []
    primes = []
    
    for i in range(1, limit):
        bools.append(True)
        
    for i in range(2, limit):
        if bools[i-2]:
            for j in range(i*2, limit + 1, i):
                bools[j-2] = False
    
    for p in range(0, len(bools)):
        if bools[p]:
            primes.append(p+2)
    
    return primes

print(sieve(13))