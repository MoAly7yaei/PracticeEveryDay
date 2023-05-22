class Persons:
    n = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Persons.n += 1
    
    def __str__():
        return 

p1 = Persons("Said", 23)
p2 = Persons("Hamza",22)
p3 = Persons("Hamza",22)

print(p3.name, p3.age)
    