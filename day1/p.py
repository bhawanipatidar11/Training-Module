import pandas as pd

d = {
    "Roll_no" : [1,2,3],
    "Name" : ["A","B","C"]
}

df = pd.DataFrame(d)

print(df.loc[0])
print(df)