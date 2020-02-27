x=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
temp=0
dict={'list':[],'sum':0}
for i in x:
    temp=0
    for j in i:
        temp=temp+j
    if dict['sum']< temp:
        dict['sum']=temp
        dict['list']=i
print(dict['list'])

