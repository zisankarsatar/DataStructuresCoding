import numpy as np

v = np.arange(0,31,3)
m = np.random.randint(0,10,(3,5))

al_getir = [1,2,3] #index numaralari
print(v[al_getir])
#[3 6 9]

satir = np.array([0,1])
sutun = np.array([1,2])
print(m[satir, sutun])
#[3 2]

#slice and fancy
print(m[0: ,[1,2]])
"""
[[2 0]
 [5 9]
 [3 3]]
"""