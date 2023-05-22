class Stack:
    
    def __init__(self,x):
        self.x = x
        
    def rev(self):
        m = 0
        y = []
        for i in range(len(self.x)):
            m = m - 1
            y.append(self.x[m])
        self.x = y 
    
    def __str__(self):
        j = 0
        rev = ""
        for j in self.x:
            rev = rev + j
        
        self.x = rev
        return self.x

user_type = input("Enter What you went to reverse: ")
user_type = list(user_type)
word = Stack(user_type)

word.rev()
print(word.__str__())
            
            
