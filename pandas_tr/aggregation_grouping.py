#Aggreation & Grouping (Toplulasma ve Gruplama)
import seaborn as sns
import pandas as pd
import numpy as np

#dfplanets=sns.load_dataset('planets')
#print(dfplanets.head())
"""
            method  number  orbital_period   mass  distance  year
0  Radial Velocity       1         269.300   7.10     77.40  2006
1  Radial Velocity       1         874.774   2.21     56.95  2008
2  Radial Velocity       1         763.000   2.60     19.84  2011
3  Radial Velocity       1         326.030  19.40    110.62  2007
4  Radial Velocity       1         516.220  10.50    119.47  2009
"""
#print(dfplanets.shape)
#(1035, 6) gozlem birimi(satir), degisken(sutun)

#print(dfplanets.sum())
"""
method            Radial VelocityRadial VelocityRadial VelocityR...
number                                                         1848
orbital_period                                       1986894.255326
mass                                                     1353.37638
distance                                                  213367.98
year                                                        2079388
"""
#print(dfplanets.count())
"""
method            1035
number            1035
orbital_period     992
mass               513
distance           808
year              1035
"""
#print(dfplanets.min())
"""
method            Astrometry
number                     1
orbital_period      0.090706
mass                  0.0036
distance                1.35
year                    1989
"""
#print(dfplanets["mass"].min())
#0.0036

"""
mean() -> ortalama
count() -> kac eleman
min()
max()
sum()
var() -> standart sapma
describe() -> tum func ile hesaplama
dropna() -> nan degerler silindi
"""

#print(dfplanets.head().describe())
"""
       number  orbital_period       mass    distance         year
count     5.0        5.000000   5.000000    5.000000     5.000000
mean      1.0      549.864800   8.362000   76.856000  2008.200000
std       0.0      265.020376   7.054234   40.630437     1.923538
min       1.0      269.300000   2.210000   19.840000  2006.000000
25%       1.0      326.030000   2.600000   56.950000  2007.000000
50%       1.0      516.220000   7.100000   77.400000  2008.000000
75%       1.0      763.000000  10.500000  110.620000  2009.000000
max       1.0      874.774000  19.400000  119.470000  2011.000000
"""
#print(dfplanets.head().describe().T)
"""
                count       mean         std      min      25%      50%      75%       max
number            5.0     1.0000    0.000000     1.00     1.00     1.00     1.00     1.000
orbital_period    5.0   549.8648  265.020376   269.30   326.03   516.22   763.00   874.774
mass              5.0     8.3620    7.054234     2.21     2.60     7.10    10.50    19.400
distance          5.0    76.8560   40.630437    19.84    56.95    77.40   110.62   119.470
year              5.0  2008.2000    1.923538  2006.00  2007.00  2008.00  2009.00  2011.000
"""

#grouping
dtgroup = pd.DataFrame({'gruplar':['A','B','C','A','B','C'],
                        'veri' : [23,45,64,26,7,98]}, columns=['gruplar','veri'])
#print(dtgroup)
"""
  gruplar  veri
0       A    23
1       B    45
2       C    64
3       A    26
4       B     7
5       C    98
"""
#print(dtgroup.groupby('gruplar').mean())
"""
gruplar  veri   
A        24.5
B        26.0
C        81.0
"""
#df=sns.load_dataset('planets').groupby("method")
#print(df.head())

dtsinavnotlari = pd.DataFrame({'gruplar':['A','B','C','A','B','C'],
                              'degisken1' : [23,45,64,26,7,98],
                              'degisken2' : [900,343,87,12,74,342]}, 
                              columns=['gruplar','degisken1','degisken2'])

#print(dtsinavnotlari.groupby('gruplar').aggregate(["min", np.median, 'max']))
"""
                degisken1            degisken2            
              min median max       min median  max
gruplar                                           
A              23   24.5  26        12  456.0  900
B               7   26.0  45        74  208.5  343
C              64   81.0  98        87  214.5  342
"""
#print(dtsinavnotlari.groupby('gruplar').aggregate({'degisken1':'min', 'degisken2':'max'}))
"""
         degisken1  degisken2
gruplar                      
A               23        900
B                7        343
C               64        342
"""