
import csv 

filename = "D:/python/trainingSession/workspace/assignment4/employees.csv"


with open(filename, 'r') as csvfile:
    myList = []
    count=0


    creader = csv.reader(csvfile) 
    creader.__next__()
    for r in creader:
        print("ALL",r)
        for i in r:
            if i=='':
                print("ININ",r)
                count=1
        if count!=1:
            print("MYYlISY",r)
            myList.append(r)
#filename2 = "D:/python/trainingSession/workspace/assignment4/chandan2.csv"
with open(filename, 'w') as wcsvfile:
        wwrriter = csv.writer(wcsvfile)
        wwrriter.__next__()
        for i in myList:
            wwrriter.writerow(i)

                
