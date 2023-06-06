import pandas as pd
import numpy as np

#List
# y = np.array(['P','A','N','D','A','S'])
# x = pd.Series(y)


#Dictionary
# x = {'x':1,'y':2,'z':3}
# y = pd.Series(x)
# print(y)

# TO copy the same value of the index
# x = pd.Series(4,index=[0,1,2,3])
# print(x)    

# to access the elements 
x = pd.Series([1,2,3,4],index=[0,1,2,3])
print(x[2])