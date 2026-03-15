#dataFrame cretion---------
import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Vandana" ,"vannu" , "priya" , "sikha" , "prena" ,"preeti"],
    "Marks": [85, 90, 95 ,55 ,66,66,77,88]
}
df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv" , index = False)
#df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)

print(df)


