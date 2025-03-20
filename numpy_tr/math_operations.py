import numpy as np
#ufunc
v = np.random.randint(-5,10,10)
print(v)
#[-3  7 -4 -2  7 -1  6 -2  9  4]
print(np.subtract(v,1))
#[-4  6 -5 -3  6 -2  5 -3  8  3]
print(np.add(v,2))
#[-1  9 -2  0  9  1  8  0 11  6]
print(np.multiply(v,3))
#[ -9  21 -12  -6  21  -3  18  -6  27  12]
print(np.divide(v,2))
#[-1.5  3.5 -2.  -1.   3.5 -0.5  3.  -1.   4.5  2. ]
print(np.power(v,3))
#[-27 343 -64  -8 343  -1 216  -8 729  64]
print(np.mod(v,2))
#[1 1 0 0 1 1 0 0 1 0]
print(np.absolute(v))
#[3 7 4 2 7 1 6 2 9 4]
print(np.sin(360)) #0.9589157234143065
print(np.cos(360)) #-0.2836910914865273
print(np.log(30)) #3.4011973816621555
print(np.log10(23)) #1.3617278360175928

#iki bilinmeyenli deklem
# 5x0 + x1 = 12
# x0 + 3x1 = 10

a = np.array([[5,1], [1,3]])
b = np.array([12,10])

x = np.linalg.solve(a,b)

print(x)