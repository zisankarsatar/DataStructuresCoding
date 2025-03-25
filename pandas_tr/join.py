import numpy as np
import pandas as pd 

arr = np.random.randint(1,99, size=(4,3))
df1= pd.DataFrame(arr, columns=['var1', 'var2', 'var3'])
df2 = df1 + 20

#print(pd.concat([df1, df2], ignore_index=True)) #index prblemi cozuldu
df2.columns = ['var1', 'var2', 'deg3'] #column lardan birinin ismi degisir

#her iki dataframe de column isimleri ayni olmayabilir
print(pd.concat([df1, df2], join='inner')) # inner= join ile ortak olan column lar calisir
'''
   var1  var2
0    31    91
1    87    75
2    93    50
3    55    59
0    51   111
1   107    95
2   113    70
3    75    79
'''

#df1 de columnlara gore birlestirme yap
print(pd.concat([df1, df2.reindex(columns = df1.columns)], ignore_index = True))
'''
   var1  var2  var3
0    31    91  75.0
1    87    75  81.0
2    93    50  92.0
3    55    59  88.0
4    51   111   NaN
5   107    95   NaN
6   113    70   NaN
7    75    79   NaN
'''

dfworkers = pd.DataFrame({'workers' : ['selim','deniz','cihan','derya']})
