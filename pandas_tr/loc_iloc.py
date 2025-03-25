import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size = (10,3))
df = pd.DataFrame(m, columns=['var1', 'var2', 'var3'])
#print(df)
'''
   var1  var2  var3
0     8     2     3
1     1    22    20
2    13     7    25
3    13    20    20
4     9     3    26
5    12     7    19
6     4    10     3
7    22    19    11
8    25    25    13
9    19    28    20
'''
#df.index = ['a','b','c','d','e','f','g','h','i','j']
#print(df)
'''
   var1  var2  var3
a    28    22     8
b    20    10    22
c    19    19    20
d    16    15    20
e     1    23    22
f    19    15     3
g    13    29    24
h    20    24    20
i    27    22    23
j     7    17     1
'''
#print(df.drop('a', axis=0, inplace=True)) #kalici degisken inplace ile
'''
   var1  var2  var3
b     8    25    18
c     4    12     8
d    16    17    27
e     1    10    28
f     9    28     8
g    20    25    29
h    25     9    12
i    16    10    26
j    17    28     7
'''
#print('var4' in df) #False

#fancy
l = ['c','e']
#print(df.drop(l, axis=0))
'''
   var1  var2  var3
a     9    21     1
b     9    25     3
d    24    28     9
f    19    23     6
g    13    27    24
h     4    28     5
i    15    20     7
j     8     9     8
'''

df['var4'] = df['var1'] / df['var2']
#print(df)
'''
   var1  var2  var3       var4
a    17    12    18   1.416667
b     2     5    19   0.400000
c     7    14     6   0.500000
d     6    10     4   0.600000
e    15    12    29   1.250000
f     7    23     6   0.304348
g     7     1    13   7.000000
h    17    13     1   1.307692
i    24    11    16   2.181818
j    28     1    14  28.000000
'''

#print(df.drop('var2', axis=1))
'''
   var1  var3       var4
a    22    28   1.571429
b     6    17   3.000000
c     4    17   0.181818
d    27    20   9.000000
e    17    21   0.850000
f    27    19   1.173913
g    28    25   3.500000
h    10     5  10.000000
i    28    10   1.000000
j    18     5   1.800000
'''

#loc = verilen kurallara bagli kalinarak (degisken ve gozlem ismi kullanarak search) te loc kullanilir
#print(df.loc[0:3])
'''
   var1  var2  var3      var4
0    18    13    14  1.384615
1     1    19    18  0.052632
2    11    19    26  0.578947
3    19     2     1  9.500000
'''
#iloc = verilen isimlerden bagimsiz, index ile secim yapilirken kullanilir
#print(df.iloc[0:3])
'''
   var1  var2  var3      var4
0    18    13    14  1.384615
1     1    19    18  0.052632
2    11    19    26  0.578947
'''

#loc
print(df.loc[0:3, "var3"])
'''
0    24
1    20
2     5
3    19
'''

#iloc
print(df.iloc[0:3]['var3'])
'''
0    24
1    20
2     5
'''