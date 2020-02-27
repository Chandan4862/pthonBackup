def functionList(list):
    max=0
    min=1001
    n=len(list)
    sum=0
    for tuple in list:
         if tuple[0]> max:
             max=tuple[0]
         if tuple[0]<min:
             min=tuple[0]
         sum=sum+tuple[0]
    average= sum/n
    finalTuple=(max,min,average)
    return finalTuple