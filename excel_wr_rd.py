import pandas as pd

df = pd.read_excel(r'北京营地汇总.xlsx', header=None)
# print(df.head())
print(df[2][1])
print(len(df.index))
print(len(df.columns))

df[1][1] = 6
# print(df)
# df.to_excel('路线.xlsx', index = False, header=None)