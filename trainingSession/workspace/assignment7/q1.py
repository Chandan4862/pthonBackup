import pandas as pd
df1 = pd.read_csv('D:/python/trainingSession/workspace/assignment7/data/pandas_test_1.csv')
print('#i. Describle the dataframe been stored. (Memory consumption, the number of null values)')
print(df1.info())  


print('#ii. How much water does each try of animal need?')
df2= df1.groupby('animal').water_need.sum()
print(df2)

print('# iii. List of IDs of animals consuming less than the average water needed.')
df3=df1[df1.water_need >df1.water_need.mean()]
print(df3['uniq_id'])

print('#iv. Total amount of water needed?')
print(df1.water_need.sum())

print('# The animal record of second largest intake of water been consumpted.')
df4= df1.sort_values('water_need', ascending=False)

# temp=0
# for i in df4.water_need:
#     if i>temp:
#         temp=i
# for i in df4.water_need:
#     if i<temp:
#         temp=i
#         break
# print(df4[df4['water_need'==temp]])

print('#vi. 3 animal records of the least water been consumpted.')

df5=df1.sort_values('water_need',ascending=True)
print(df5.iloc[0:3])


