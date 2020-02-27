import pandas as pd
import us
df=pd.read_csv('D:/python/trainingSession/workspace/assignment7/data/pandas_test_2.csv')
# print('Display the first few rows and the DataFrame info.')
# print(df.head())

# print('Re-read the data in such a way that all date columns are identified as dates and the earthquake id is used as the index')
# df1=pd.read_csv('D:/python/trainingSession/workspace/assignment7/data/pandas_test_2.csv',parse_dates=['time'])
# print(df1.head().info())

# print('iii. Use describe to get the basic statistics of all the columns')
# print(df1.describe())

# print('iv. Use sort_values to get the top 20 earthquakes by magnitude')
df['country']=df.sort_values('mag', ascending=False)['place'].str.split(",", n = 1, expand = True)[1]
df['place']=df.sort_values('mag', ascending=False)['place'].str.split(",", n = 1, expand = True)
# print(df.iloc[0:5])

# print("Extract the country using Pandas text data functions")
# print(df.iloc[0:5])

# print('Find the 10 states / countries with the highest number of earthquakes')
# print(df.groupby('country')['country'].value_counts().sort_values(ascending=False).iloc[0:10])

# print('Find the top 10 states / countries where the strongest earthquakes occured')
# print(df.sort_values('mag',ascending=False)[['country','mag']].iloc[0:10])

# print('Find the top 10 states / countries where the weakest earthquakes occured')
# print(df.sort_values('mag',ascending=True)[['country','mag']].iloc[0:10])

# print('Read the us documentation to figure out how to create a list of state names')
# state_names = [state.name for state in us.states.STATES]
# print(pd.Series(state_names).str.upper())

print('Write a function to check whether a string is a US state name.')
def check_State(stri):
    stri=stri.strip()
    isState= us.states.lookup(stri)
    return us.states.lookup(stri)

## state=input("Enter state name\n")
## print(check_State(state))

# print('Use Pandas apply function to apply this to each row of the country name series')
# df = df.dropna(axis = 0, how ='any') 
# df['isUsState'] = df.country.apply(check_State)

# print(df[['country','isUsState']].iloc[0:5])