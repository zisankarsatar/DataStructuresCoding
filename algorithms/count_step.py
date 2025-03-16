#google
#recursive method
#problem explanation
"""
Suppose you want climb a staircase of N steps, and on each step you can take either staircase? For example, if you wanted to climb 4 steps, 
vou can take the following 
•⁠  ⁠1) 1, 1, 1, 1
•⁠  ⁠2) 1, 1, 2
•⁠  ⁠3) 1, 2, 1
•⁠  ⁠4) 2, 1, 1
•⁠  ⁠5) 2,2

"""

def countStep(n):
    #base case
    if n == 1:
        print(1)
        return 1
    
    #base case
    if n == 2:
        print(2)

        return 2
    
    return countStep(n-1) + countStep(n-2)


print(countStep(5))