filename = "D:/python/trainingSession/workspace/assignment4/logger.txt"
def logError(err):
    with open(filename,'a') as f:
        f.write(err+ "\n")

def logInfo():
    with open(filename,'r') as r:
        data= r.read()
        print(data)
