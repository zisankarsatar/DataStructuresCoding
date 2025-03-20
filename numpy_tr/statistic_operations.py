import numpy as np
v = np.arange(-4, 30, 3)
print(v) #[-4 -1  2  5  8 11 14 17 20 23 26 29]
print(np.mean(v)) #12.5 ortalama
print(v.sum()) #150 tum elemanlar toplama
print(v.min()) #-4 min deger
print(v.max()) #29 max deger
#Varyans
print(np.var(v)) #107.25 
#standart sapma
print(np.std(v)) #10.35615758860399


