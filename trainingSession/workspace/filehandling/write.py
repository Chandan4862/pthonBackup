print("Enter String to be wrtitten")
str= input()
with open("D:/python/trainingSession/workspace/filehandling/demo.txt","a") as textFile:
    textFile.write(str)

with open("D:/python/trainingSession/workspace/filehandling/demo.txt","r") as textFile:
    print(textFile.read())