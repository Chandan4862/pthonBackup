
import csv 



mydict =[{'employee_name': 'Chandan', 'employee_code': '1670', 'employee_team': 'Core', 'appraiser': 'Anand'}, 
		{'employee_name': 'Rohan', 'employee_code': '9673', 'employee_team': 'AppStudio', 'appraiser': 'Anand'}, 
		{'employee_name': 'Suyog', 'employee_code': '', 'employee_team': 'E-pet', 'appraiser': 'Radhakishan'}, 
		{'employee_name': 'Raju', 'employee_code': '234', 'employee_team': 'E-pet', 'appraiser': 'Deepak'}, 
		{'employee_name': 'BabuRao', 'employee_code': '5423', 'employee_team': 'Course Def', 'appraiser': 'Vijay'}, 
		{'employee_name': '', 'employee_code': '4567', 'employee_team': 'Course Def', 'appraiser': 'Ajit'}]
fields = ['employee_name', 'employee_code', 'employee_team', 'appraiser'] 


filename = "D:/python/trainingSession/workspace/assignment4/employees.csv"


with open(filename, 'w') as csvfile:

	writer = csv.DictWriter(csvfile, fieldnames = fields) 

	writer.writeheader() 

	writer.writerows(mydict) 
