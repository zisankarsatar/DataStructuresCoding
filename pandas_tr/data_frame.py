import pandas as pd
import numpy as np

liste = [1,2,45,6,4,3]

pd.DataFrame(liste, columns=['degisken ismi'])

arr = np.arange(1,10).reshape(3,3)
df = pd.DataFrame(arr, columns=['var1','var2','var3'])
print(df)
"""
   var1  var2  var3
0     1     2     3
1     4     5     6
2     7     8     9
"""
df.columns = ('deg1','deg2','deg3')
print(df)
"""
   deg1  deg2  deg3
0     1     2     3
1     4     5     6
2     7     8     9
"""
print(type(df))
print(df.axes)
print(df.shape)
print(df.ndim)
print(df.values)
print(df.head())
print(df.tail(1))