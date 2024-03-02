import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('pokemon_data.csv')

#read each row
# for index,row in df.iterrows():
#     print(index,row['Name'])

# print(df.loc[df['Legendary'] == "True"])

# print(df.describe())

#sorting
# print(df.sort_values(['Type1','HP'],ascending=[1,0]))
# print(df.columns)

#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# df=df.drop(columns=['Total'])

df['Total'] = df.iloc[:,4:10].sum(axis=1)
# print(df.head(5))

df['Total'].plot()
print(plt.show())