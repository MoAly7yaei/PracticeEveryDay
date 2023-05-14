

string= input("Password: ")

valid = 8 <= len(string)

u,l,sc = 0,0,0

for i in range(len(string)):
    
    
    """
    valid = (valid and ( (string[i].islower() or
                          string[i].isupper() and
                         (string[i].isdigit() or string[i].ischar()) and
                         (string[i] == "#" or "$" or "#" or "_"))))
                         """
    if (valid and (string[i].isupper() or string[i].islower())) == True:
        
        u += 1
    
    elif (valid and (string[i].isdigit())) == True:
        l += 1
    
    elif (valid and (string[i] == "#" or "$" or "#" or "_")):
        sc +=1
    
if u >= 1 and l >= 1 and sc >= 1:
        
    print("Valid Password")

else:
    print("invalid Password")        
    


