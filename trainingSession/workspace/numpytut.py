import numpy as np

arr= np.array([(1,2,4),(4,5,6),(6,7,8),(9,3,5)])
arr1=np.array([(1,2,4),(4,5,6),(6,7,8),(9,3,5)])
# print(arr.ndim) #dimension
# print(arr.itemsize) #size each element occupies
# print(arr.dtype) #data type
# print(arr.size)#size of array i.e number of elements
# print(arr.shape) #shape of aray(rows,column)
# brr= arr.reshape(3,4) #reshape to 3 rows and 4 column
# print(brr)

#Slicing
# print(arr[0:,2]) #all values at index 2
# print(arr[0:1,2]) # values at index 2 upto 2 rows
#linSpace
# ls = np.linspace(1,100,5)
# print(ls) #5 values between 1,100 equally spaced
#max min and sum => 9,1,60
# print(arr.sum())
# print(arr.max())
# print(arr.min())

#axis: column is 0th axis and row is 1st axis

# print(arr.sum(axis=0)) #print sum of all colmn
# print(arr.sum(axis=1)) #print sum of all rows

#find square root
#print(np.sqrt(arr))
#find standard deviation
# print(np.std(arr))

#Concat two array
#1. vertical stack
print(np.vstack((arr,arr1)))
#2. horizontal stack
print(np.hstack((arr,arr1)))