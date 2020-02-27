# . Using - "VSP1K_CLI_COMMANDS.csv" - Write a script to extract top 10 occuring unique tokens (words only) 
# from the "Hidden command" column.

import pandas as  pd 
file = pd.read_csv('D:/python/trainingSession/workspace/test/VSP1K_CLI_COMMANDS.csv')
print(file['Hidden command'].unique()[0:10])