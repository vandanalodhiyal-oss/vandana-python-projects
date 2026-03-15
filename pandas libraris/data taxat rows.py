#1 - Understand the data set
#2 - identify the problems
#3 - plan nest steps

#head method() , tail method() , info()
#head(n)-----first row display -----n(number)
#tail(n)------ last row

import pandas as pd

df = pd.read_csv("_employe.csv - Sheet1.csv")

print('Display 5 rows of firt')
print(df.head(5))
print('Display 5 rows of last')
print(df.tail(5))

