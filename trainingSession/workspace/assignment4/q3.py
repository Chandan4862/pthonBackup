# Write a program for basic 
# JSON file handling operations like Writing, Reading, Updating
import json

# filename = "D:/python/trainingSession/workspace/assignment4/chandan.txt"
data1 =[
    {"name":"Chandan", 
   "age":23, 
    "Salary":25000},
    {"name":"Rohan", 
   "age":23, 
    "Salary":25000}
]


#write
f=open("D:/python/trainingSession/workspace/assignment4/chandan.json", "w")
fdata=json.dumps(data1)
f.write(fdata)
f.close()


#read
f=open("D:/python/trainingSession/workspace/assignment4/chandan.json", "r")
data= json.load(f)
print(data)
f.close()
