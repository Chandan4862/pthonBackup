#  Create package "Strings" that will contain all basic operations of Strings
# Ex: Concat, Substring, Trim, Length, Find palindrome strings, Uppercase, lowercase, captilization
# Minimum 5 functions required in a package

from stringOperation import operation as o

str1 = "Hello  "
str2="Chandan"
stringToFind="Hell"
print("lowerCase::",o.lowerCase(str1))
print("UpperCAse::",o.upperCase(str2))
print("CONCAT::",o.concat(str1,str2))
print("SubString::",stringToFind,"is",o.find(str1,stringToFind),"in",str1)
print("Trim::",o.trim(str1))
