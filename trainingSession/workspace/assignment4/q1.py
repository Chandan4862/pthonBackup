from logger import log
try:
    import chandan
except ImportError:
    log.logError("Import Error")

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
    log.logError("Syntax Error")

#write
try:
    json.dumps(Chandan)
except NameError:
    log.logError("Pass correct Data")
except TypeError:
    log.logError("TYPE ERROR")

with open(filename, 'w') as csvfile:
    writer = csv.writer(csvfile) 
    try:
        for i in writer:
            print(i)
    except TypeError:
        log.logError("writer object is not iterable")
try:
    f = open ( "chandan.txt", 'r' )
except FileNotFoundError:
    log.logError("No such file or directory")

##VIEW LOG INFO
print("DATA FROM LOG FILE")
log.logInfo()




