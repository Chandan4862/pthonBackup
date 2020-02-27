import pandas as pd  
import numpy as np
import random  as r
import sys
# countryNames = ['Afghanistan','Albania','Algeria','Andorra','Angola',
#         'Antigua and Barbuda','Argentina','Armenia','Australia', 'Austria']
# populationCount = [38041754, 2880917, 43053054, 77142, 31825295, 
#          97118, 44780677, 2957731, 25203198, 8955102]
# arr = pd.Series(populationCount,countryNames)
# print(arr)
#  arr1=pd.Series(countryNames)


# aSeriesofNumbers=pd.Series([4,11,21,36],dtype='int8')
# print(sys.getsizeof(aSeriesofNumbers))
# print(len(dir(aSeriesofNumbers)))
# print(aSeriesofNumbers[0:3])

# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data)
# print(s)

# arr2=pd.Series(5., index = ['Afghanistan','Albania','Algeria','Andorra','Angola',
#         'Antigua and Barbuda','Argentina','Armenia','Australia', 'Austria'])
# print(arr2.tail())
# print(arr2.head())
# print(arr2.mean())
# print(arr2==5.0)#check 


# arr4=[]
# for i in range(100):
#     arr4.append(r.randint(0,101))
# arr5 = pd.Series(arr4)
# print(arr5[arr5%5==0])

# aDataFrame = pd.DataFrame({'country names':countryNames,"Population":populationCount})
# print(aDataFrame.xs('country names',axis=1))
# extra= pd.DataFrame({'country names':["India"],"Population":[10.]})

# countries19= extra.append(aDataFrame,ignore_index=True) #avoid duplicate value
# # print(countries19)
# print(countries19.describe())

# raw_data_1 = {
#         'subject_id': ['1', '2', '3', '4', '5'],
#         'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
#         'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

# raw_data_2 = {
#         'subject_id': ['4', '5', '6', '7', '8'],
#         'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
#         'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

# raw_data_3 = {
#         'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
#         'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
# df1= pd.DataFrame(raw_data_1)
# df2= pd.DataFrame(raw_data_2)
# df3= pd.DataFrame(raw_data_3)
# df4=pd.concat([df1,df2],ignore_index=True, axis=0)
# final= pd.merge(df3,df4,on='subject_id', how='right')
# final.index= final['first_name']+'_'+final['last_name']
# #OR
# # final.setIndex
# print(final)

