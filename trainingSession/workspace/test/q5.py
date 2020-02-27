#Print addition of prime numbers between 50 to 100.

brr=[]
sum=0
for i in range(50,101):
    brr.append(i)

for i in brr:
    if i > 1:
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
           sum=sum+i
    
    
print("Sum is ",sum)
