# file= open("D:/python/trainingSession/workspace/filehandling/demo.txt","r")
# print(file.readline())

with open("D:/python/trainingSession/workspace/filehandling/demo.txt") as textFile:
    lines= textFile.read()
    print(lines)

