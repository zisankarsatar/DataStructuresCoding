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
#reshape, 
a = np.arange(1,10).reshape((3,3))
#print(a)
"""
vektorel -> matris 
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

a = np.arange(0,10)

#print(a.ndim)
#print(a)
b = a.reshape((2,5))
#print(b)
"""
[0 1 2 3 4 5 6 7 8 9]
[[0 1 2 3 4]
 [5 6 7 8 9]]
"""
#concatenation(birlestirme)
x = np.array([1,2,3])
y = np.array([4,5,6])
z = np.array([7,8,9])

a = np.concatenate([x,y,z])
#print(a)
"""
[1 2 3 4 5 6 7 8 9]
"""

#iki boyut
a = np.array([[1,2,3],
             [4,5,6]])

b = np.concatenate([a,a])
#print(b)
"""[[1 2 3]
 [4 5 6]
 [1 2 3]
 [4 5 6]]"""
 
c = np.concatenate([a,a], axis=1)
#print(c)
"""
[[1 2 3 1 2 3]
 [4 5 6 4 5 6]]
"""
# axis = 1 satir

#spliting
x = np.array([1,6,3,4,99,5,4,3])
np.split(x, [3,5])

a,b,c = np.split(x, [3,5])
#print(a)
#[1 6 3]

#iki boyutlu ayirma
m = np.arange(16).reshape(4,4)
ust, alt = np.vsplit(m,[2])
#print(ust)
"""
[array([[0, 1, 2, 3],
       [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
       [12, 13, 14, 15]])]
       """

m = np.arange(16).reshape(4,4)
x = np.hsplit(m,[2])
#print(x)
"""
[array([[ 0,  1],
       [ 4,  5],
       [ 8,  9],
       [12, 13]]), array([[ 2,  3],
       [ 6,  7],
       [10, 11],
       [14, 15]])]
       """
       
#sorting
v = np.array([2,1,4,3,5])
#print(np.sort(v)) 
v.sort() # koklu degisti
#print(v)

#iki boyutlu siralama
m = np.random.normal(20,5,(3,3))
print(np.sort(m, axis=1)) #stair
"""
[[ 8.99770719 13.38972746 29.82296577]
 [15.47622186 16.99417231 17.8052793 ]
 [21.35563598 22.90166844 27.80617363]]
"""
print(np.sort(m, axis=0)) #stun
"""
[[19.10570863 19.41751221 12.40408062]
 [22.76558711 27.77886295 13.83176311]
 [24.80316324 30.37630167 25.10304812]]
"""