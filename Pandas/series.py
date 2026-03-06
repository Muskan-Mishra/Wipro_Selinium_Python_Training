#Pandas - it is high performance and data manipulation and data analysis tool
#developed in 2008 Mckinnley
#data frames object
#list , csv, josn, pdf

#series -  A one-dimensional labeled homogeneous array, size immutable
#DataFrames is a 2dimensional labeled ,size-mutable tabular structure with potentially heterogeneously typed columns.


#creation of series
import pandas as pd
data =['roy','45','male','4.5']
series = pd.Series(data, index=['name','age','gender','rating'])
print(series)

#create series using custom  index

data =[100,200,300]
s = pd.Series(data,index=['a','b','c'])
print(s)

#create series from dictionary
data ={'a':1,'b':2,'c':3}
s = pd.Series(data)
print(s)

#create series numpy array
import  numpy as np
arr = np.array([5,10,15])
s = pd.Series(arr)
print(s)

#crete empty series
s = pd.Series(dtype=float)
print(s)

#crete a series with specific datatype
data =[1,3,2]
s = pd.Series(data,dtype=float)
print(s)