
def isAppend(source,destination):
        text='Do not append.'
        # with open("D:/python/trainingSession/workspace/test/source.txt") as source:
        text1= source.read()
        # with open("D:/python/trainingSession/workspace/test/destination.txt","r+") as destination:
        text2= destination.read()
        if text2.endswith('###Okay Python###') == False:
                text= text1+text2
                destination.write(text1)
        print(text)
# with open("D:/python/trainingSession/workspace/test/source.txt") as source:
# with open("D:/python/trainingSession/workspace/test/destination.txt","r+") as destination:
source = open("D:/python/trainingSession/workspace/test/source.txt")
destination= open("D:/python/trainingSession/workspace/test/destination.txt","r+")
isAppend(source,destination)
