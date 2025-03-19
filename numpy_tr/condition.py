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
print(v/5)
print(v**2)