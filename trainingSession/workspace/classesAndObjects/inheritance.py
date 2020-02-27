class C1:
    def simFunc(slef,a,b):
        return a+b
class C2:
    def simFunc(self,a,b):
        return a*b
class Derived(C1,C2):
    def simFunc(self,a,b):
        return a/b
d=Derived()
print(d.simFunc(10,20))