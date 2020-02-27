import re
str = str(input("Enter string: ")) 
regexObject = re.compile(r'#[0-9]+')
string = regexObject.findall(str)
output=string[0].split("#")
print(output[1])