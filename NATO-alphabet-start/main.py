import pandas as pd

user = input()
data = pd.read_csv("python/NATO-alphabet-start/nato_phonetic_alphabet.csv")
dic1 = {row.letter:row.code for (item,row) in data.iterrows()}
user_input = [i.upper() for i in user]
list1 = [dic1.get(i) for i in user_input]
for i in range(0,len(list1)):
    print(f"{user_input[i]} - {list1[i]}")