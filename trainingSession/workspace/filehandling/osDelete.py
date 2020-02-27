import os

if os.path.exists("D:/python/trainingSession/workspace/filehandling/demo.txt"):
    os.remove("D:/python/trainingSession/workspace/filehandling/demo.txt")
    print("DELTED")
else:
    print("FILE not exits")