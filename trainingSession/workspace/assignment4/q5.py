try:
    import chandan
except ImportError:
    print("Module not Found")

import json
import csv

filename = "D:/python/trainingSession/workspace/assignment4/chandan.txt"
try:
    data1 =[
    {"name":"Chandan", 
   "age":23, 
    "Salary":25000},
    {"name":"Rohan", 
   "age":23, 
    "Salary":25000}
    ]
except SyntaxError:
    print("Syntax Error")

#write
try:
    json.dumps(Chandan)
except NameError:
    print("Pass correct Data")
except TypeError:
    print("TYPE ERROR")

with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile) 
    try:
        for i in writer:
            print(i)
    except TypeError:
        print("CUSTOM MSG: "+"writer object is not iterable")
try:
    f = open ( "chandan.txt", 'r' )
except FileNotFoundError:
    print("No such file or directory")




