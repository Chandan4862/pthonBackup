def lowerCase(str):
    str=str.lower()
    return str
def upperCase(str):
    str= str.upper()
    return str
def concat(str1,str2):
    str1=str1+ " "
    return str1+str2
def find(str1,str2):
    if str2 in str1:
        return "present"
    else:
        return "Not present"
def trim(str):
    return str.strip()
