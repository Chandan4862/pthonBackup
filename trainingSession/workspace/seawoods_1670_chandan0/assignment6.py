'''Write a program to print the below output.
     *
    *
   *
  *
 *
 *
  *
   *
    *
     *

Hint - In built function Range. (Ascending / Decending)
'''
# flag=0
# for i in range (8,0,-1):
#     j=1
#     while(j < (9)):
#         if j>=4:
#             if j==i:
#                 print("*",end="")
#             else:
#                 print(" ",end="")
#         j=j+1
#     print('')



x=4
for i in range(5,0,-1):
    for j in range(0,5,+1):
        print(" ",end='')
        if x==j:
            print("*",end='')
    x=x-1
    print("")

x=1
for i in range(1,6,+1):
    for j in range(1,6,+1):
        print(" ",end='')
        if j==x:
            print("*",end='')
    x=x+1
    print("")

