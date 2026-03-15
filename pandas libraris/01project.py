#head---starting 5 row read
import pandas as pd

df = pd.read_csv("pandas libraris/Employee.data - Sheet1.csv")
print(df.head())


print()
#summary of numeric colums
print(df.describe())
print()
print("Average Salary:", df["Salary"].mean())  # Average salary
print("Max Age:", df["Age"].max())    # Maximum Age
print("Min Salary:", df["Salary"].min())   # Minimum Salary
print("Most common Department:", df["Department"].mode()[0])    # Mode of Department


#filtering row-------employee with salary>50000
high_salary = df[df["Salary"] > 50000]
print(high_salary)