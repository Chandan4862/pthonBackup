def nlist(*listArray):
    i = 0
    resultList = listArray[i]
    while i < len(listArray)-1:
        resultList = listSum(resultList, listArray[i+1])
        i = i+1
    return resultList



def listSum(listA,listB):
    list=[]
    final=[]
    n=len(listA[0])
    m=len(listA)
    for j in range(m):
        for i in range(n):
            list.append(listA[j][i]+listB[j][i])
        final.append(list)
        list=[]
    return final
            