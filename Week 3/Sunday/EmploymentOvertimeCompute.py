class Employee:
    
    new_dep = ""
    def __init__(self,name,Id,dep,salery,hw,h):
        self.name = name
        self.dep = dep
        self.salery = salery
        self.Id = Id
        self.hw = hw
        self.h = h
    
    def salery_print(self):
        return f"The salery for Mr/Ms {name} is : {salery}"
    
    def set_dep(self,new_dep):
        self.dep = new_dep
        
    def __str__(self):
        
        return f"Name: {self.name}, Dep: {self.dep}, salery: {self.overtime()}"
    
    def overtime(self):
        over = self.hw - self.h
        salary_overtime = self.salery + over * (self.salery/50)

        return salary_overtime
        
        
        
emp1 = Employee("Adam",15179,"Research",9000,70,65)

print(emp1.__str__())

emp1.set_dep("IT Department")

print(emp1.__str__())



    
    