# i. Write a program that accepts a sentence and calculate the number of letters and digits.
print("Enter String")
str=input()
dic={'letters':0,'digits':0}
for i in str:
    if i.isalpha()== True:
        dic['letters'] += 1
    if i.isdigit()== True:
        dic['digits'] += 1
print('LETTERS',dic['letters'])
print("DIGITS",dic['digits'])
    