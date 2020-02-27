list=[{"{name":"chandan","age":22,"sal":10000},
    {"{name":"mrunal","age":32},
    {"{name":"mama","age":25,"sal":1000},
    {"{name":"rohan","sal":10000}]
sumAge=0
count=0
sumsal=0

for dict in list:
        if "age" in dict:
            sumAge=sumAge+dict['age']
            count=count+1
        if "sal" in dict:
            sumsal=sumsal+dict['sal']
print("average age is:",sumAge/count,'\n')
print("Sum Salary is:",sumsal,'\n')

            