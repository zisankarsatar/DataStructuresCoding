import numpy as np

#basic array
a = np.array([3,4,5,2])
#print(type(a))

a = np.array([3.14,4,5,2])
#print(a)
# cikti -->> [3.14 4.   5.   2.  ] 
#herhangi bir eleman ondakli ise digerleride ondakliya ceviriliyor. Numpy array in sabit veri tipi ozelliginden dolayi
a = np.array([3.14,4,5,2], dtype='int')
#print(a)
#integer a ceriliyor tum liste elemanlari

a = np.zeros(10)
#print(a)
#sifirdan 10 elemanli elemanlarinin herbiri 0 olan bir liste

a = np.ones((3,5), dtype='int')
#print(a)
# 3 satir, 5 sutunluk 1 den olusan matris

a = np.full((3,5), 3)
#print(a)
# 3 satir, 5 sutunluk 3 den olusan matris

a = np.arange(0,31,3)
#print(a)
# 0 dan 31 e kadar 3 er 3 er artan bir liste

a = np.linspace(0,1,10)
#print(a)
# Odan 1e 10 sayi

a  = np.random.normal(10,4,(3,5))
#print(a)
#ortalamasi 10, standart sapmasi 4 olan 3e 5lik matris

a  = np.random.randint(0,10,(3,4))
#print(a)
# 0dan 10a 3,4luk integer matirs

##Functions
a = np.arange(1,10).reshape((3,3))
print(a)
"""
vektorel -> matris 
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

a = np.arange(0,10)

print(a.ndim)
print(a)
b = a.reshape((2,5))
print(b)
"""
[0 1 2 3 4 5 6 7 8 9]
[[0 1 2 3 4]
 [5 6 7 8 9]]
"""
