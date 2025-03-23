import pandas as pd

seri = pd.Series([10,88,23,6,789])
print(seri)
"""
0     10
1     88
2     23
3      6
4    789
dtype: int64
"""
print(type(seri))
#pandas.core.series.Series
print(seri.axes)
#[RangeIndex(start=0, stop=5, step=1)]
print(seri.dtype)
#int64
print(seri.size)
#5
print(seri.ndim)
#1
print(seri.values)
#[ 10  88  23   6 789]
print(seri.items())
print(seri.keys)
print(seri.index)
print(seri.head(3))
"""
0    10
1    88
2    23
dtype: int64
"""
print(seri.tail(2))
"""
3      6
4    789
dtype: int64
"""

#index ismlendirmesi ve slice islemleri
x = pd.Series([34,23,5,2,76,91], index = ['a',1,'m','d',4,7])
print(x)
"""
a    34
1    23
m     5
d     2
4    76
7    91
dtype: int64
"""
print(x["a":"d"])
"""
a    34
1    23
m     5
d     2
dtype: int64
"""
#sozluk uzerinden liste olusturmak
sozluk = pd.Series({"reg":10, "log":11, "cart":12})
print(sozluk)
"""
reg     10
log     11
cart    12
dtype: int64
"""
print(pd.concat([sozluk,seri]))
"""
reg      10
log      11
cart     12
0        10
1        88
2        23
3         6
4       789
dtype: int64
"""