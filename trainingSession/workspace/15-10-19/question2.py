employees=[
       {'name':'Joel', 'salary': 25, 'experience': 2, 'status': 'Okay'},
       {'name':'Imtiyaz', 'experience': 2, 'status': 'Okay'},
       {'name':'Chandan', 'experience': 1, 'status': 'Okay','salary': 24},
       {'name':'Rohan', 'experience': 1, 'status': 'Okay','salary':21},
       {'name':'Suyog', 'experience': 2, 'status': 'NotOkay'}
    ]
count=0
sum=0

for employee in employees:
    if "salary" not in employee:
        employee["salary"]=10*employee["experience"]
        if employee["status"] == 'Okay':
            employee["salary"]=employee["salary"]+5
            employee["status"]="HR APPROVAL"
            print("111",employee)
            print("Updated Salary-","name:",employee["name"],"salary:",employee["salary"],"status:",employee['status'])
    else:
        count=count+1
        sum= sum+employee["salary"]
print("Avg. Salary of employees if 'status'is 'Okay' ::",sum/count)

        



# for employee in employees:
#     if "salary" in employee:
#         employee['salary'] =employee['salary']+ 10*employee['experience']
#         if employee['status'] == 'Okay':
#             count=count+1
#             employee['salary']=employee['salary']+ 5
#             sum=sum+employee['salary']
#         employee['status']='HR Approval'
#         print("Updated Salary-","name:",employee["name"],"salary:",employee["salary"],"status:",employee['status'])
# print("Avg. Salary of employees if 'status'is 'Okay' ::",sum/count)