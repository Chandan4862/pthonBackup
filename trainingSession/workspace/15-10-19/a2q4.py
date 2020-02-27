x=[(3,1),(4,2),(9,0),(6,-2),(-9,-1)]
temp=10
for i in x:
    if temp>i[1]:
        temp=i[1]
print(temp)
