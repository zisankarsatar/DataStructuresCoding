import numpy as np
 
a = np.array([1,2,3,4,5,6,7,8,9])

print(a[0::2])
#[1 3 5 7 9]

m = np.random.randint(0,10,(3,5))
print(m[:,0])
#[2 7 0]

print(m[:,1])
#[6 3 3]

print(m[0,:])
#[2 6 3 2 0]
print(m[0])
#[2 6 3 2 0]

print(m[1,:])
#[7 3 4 5 7]

print(m[0:2,0:3])
"""
[[2 6 3]
 [7 3 4]]
"""

print(m[::,:2])
"""
[[2 6]
 [7 3]
 [0 3]]
"""

print(m[1:3,0:2])
"""
[[7 3]
 [0 3]]
"""