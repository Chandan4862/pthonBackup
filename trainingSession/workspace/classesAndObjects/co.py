class Animal:
    kind ="Dog"
    def __init__(self,name):
        self.name=name

d = Animal('Fido')
e= Animal('Buddy')

print(d.name)
print(e.name)
print(d.kind)
print(e.kind)