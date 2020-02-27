#Create an array of 15 zeros,15 ones, 15 fives

import numpy as np

arr1 = np.zeros((15),dtype=int) 
print(arr1)
arr2 = np.ones((15),dtype=int)
print(arr2)

arr3 = np.full((15),5,dtype=int)
print(arr3)
#print(np.append(arr3,[arr2,arr1],axis=1))
