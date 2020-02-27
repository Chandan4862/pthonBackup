# 1. Consider you have 3 list object each containing a list of integers. Print the addition 
# of the data structure. Define a function taking only 2 list objects as input. No external 
# library should be used.
# *Hint. All list objects are of the same dimension. The 3 list objects may be identical.
# For eg. 
#     Input => List_A = [[1,2,3], ...], List_B = [[1,2,3], ...], List_C = [[1,2,3], ...]
#     Output => [[3,6,9], ...]

from listPackage import list as l
        


List_A = [[1,2,3], [4,5,6],[7,8,9]]
List_B = [[1,2,3], [4,5,6],[7,8,9]]
List_C = [[1,2,3], [4,5,6],[7,8,9]]
result=l.listSum(List_A,List_B)
finalresult=l.listSum(result,List_C)
print("The sum is::",finalresult)