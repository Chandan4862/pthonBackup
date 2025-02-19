# importing csv module  
import csv
# csv file name 
filename = "D:/python/trainingSession/workspace/csv/aapl.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile:

	# creating a csv reader object 
	csvreader = csv.reader(csvfile)
	
	# extracting field names through first row 
	fields = csvreader.__next__()

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

# printing the field names 
print(fields)

# printing first 5 rows 
print('\nFirst 5 rows are:\n') 
for row in rows[:5]:
	print(row)
	# parsing each column of a row 
	for col in row:
		pass 
		#print("%10s"%col), 
		# print('\n') 
