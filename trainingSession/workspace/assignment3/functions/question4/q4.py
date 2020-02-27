import random
from EvenOddList import list as l
list = []
# populating list with tuple of single element of length 100
for x in range(100):
    y = random.randint(999, 9999)
    list.append(y)
finalResult=l.EvenOdd(list)
print(finalResult)
