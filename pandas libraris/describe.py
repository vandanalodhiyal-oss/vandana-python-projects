#step-1 sample data frame

import pandas as pd

data={
    "Name":['vandana','preet','seeta','geeta','preeti','sikha', 'aadi','priya'],
    "Salary":[20000,40000,50000,15000,10000,40000,30000,30000],
    "Age": [21, 22, 33,43,23,25,26,30]
    }
df=pd.DataFrame(data)
print("Sample DataFrame")
print(df)
print('Descriptive Statistics')
print(df.describe())