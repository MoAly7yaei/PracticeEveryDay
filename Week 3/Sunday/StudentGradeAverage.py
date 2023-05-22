"""
Inheritance - OOP
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Student(Person):
    def __init__(self,name, age,grade):
        super().__init__(name, age)
        self.grade = grade
    
    def avg_grade(self):
        avg = 0
        j = 0
        s = 0
        for mark in self.grade:
            j += 1
            s = s + mark
            avg = s / j
        
        return avg
    
std1 = Student("Ali",22,[3,3,3,4,4,3,3,4])

print(std1.avg_grade())
        
    
        