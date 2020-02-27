#Contructor or method overriding is not supported

class A:
    name:"mama"
    def __init__(self):
        self.name="chandan"
    def __new__(self,name):
        self.name="Vilas"
d=A("Rohan")
print(d.name)
print(dir(d))