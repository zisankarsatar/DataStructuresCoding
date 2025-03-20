import numpy as np

v = np.array([1,2,3,4,5,6])

print(v<3)
#[True True False False False False]

print(v[v<3])
#[1,2]

print(v[v>=3])
#[3,4,5,6]

print(v[v != 3])
#[1,2,4,5,6]

print(v[v == 3])
#[3]

print(v*2)
#[ 2  4  6  8 10 12]

print(v/5)
#[0.2 0.4 0.6 0.8 1.  1.2]

print(v**2)
#[ 1  4  9 16 25 36]