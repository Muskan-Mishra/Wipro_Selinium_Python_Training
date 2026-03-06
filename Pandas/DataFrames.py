import pandas as pd
#DataFrame is 2-dimensional labeled data structure (rows & columns)
#like an excel SQL tables

#create DataFrame from list Dictionaries

data= [
    {"Name":"Ram", "Age":25},
    {"Name":"Sam","Age":30},
    {"Name":"John","Age":28},
]
df =pd.DataFrame(data)
print(df)

#create DataFrame from Dictionary of series
s1 = pd.Series([1,2,3])
s2 = pd.Series([4,5,6])

df = pd.DataFrame({"A":s1,"B":s2})
print(df)

#create DataFrame from Numpy Array
import numpy as np

arr = np.array([[1,2],[3,4],[5,6]])
df = pd.DataFrame(arr,columns=["A","B"])
print(df)

#create dta frames using CSV file
df = pd.read_csv("employees.csv")
print(df)

#create empty df
df=pd.DataFrame()
print(df)

#create DataFrame with custom Index
data ={
    "Name":["Ram","Sam"],
    "Age":[25,30]
}
df = pd.DataFrame(data, index=["Emp1","Emp2"])
print(df)









