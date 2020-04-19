import pandas as pd
df = pd.read_csv('hw0419.csv')
print(df)

#讀取後放入DaataFrame
select_df = pd.DataFrame(df)
filled_value = select_df.fillna(0)
print(filled_value)
print("---")