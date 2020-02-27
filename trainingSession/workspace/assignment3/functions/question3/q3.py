import random
from randomList import list as l
list = []
# populating list with tuple of single element of length 100
for x in range(100):
    y = random.randint(0, 1000)
    list.append(tuple([y]))
finalResult=l.functionList(list)
print(finalResult)
