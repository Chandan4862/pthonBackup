import xlrd 

loc = ("D:/python/trainingSession/workspace/bank/bank.xlsx")
dict={}
list=[]
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
TotalTransc=0
TotalAmt=0
# For row 0 and column 0 
for i in range(sheet.nrows):
    if "FOOD" in sheet.cell_value(i, 1) or "food" in sheet.cell_value(i, 1) or "UPI-SHANKAR" in sheet.cell_value(i, 1):
        dict["Transactioin"]=sheet.cell_value(i, 1)
        dict["Amount"]=sheet.cell_value(i, 4)
        list.append(dict)
        dict={}
for transc in list:
    TotalTransc = TotalTransc +1
    TotalAmt= TotalAmt + transc["Amount"]
    print(transc)
print("Total Transc",TotalTransc,"Total Amount Spent on Food",TotalAmt)