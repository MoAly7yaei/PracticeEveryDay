lst = ["said,40","Majid,30","Salim,22","Ali,18","Sultan,28"]
lst2 = []
names = []
output = []

for i in lst:
    data = i.split(",")
    lst2.append(int(data[1]))
    names.append(data[0])


x = 0
def sorting(names,lst2):
    for k in range(1,len(lst2)):
        key = lst2[k]
        key2 = names[k]
    
        x = k - 1
        while x >= 0 and key < lst2[x]:
            
            lst2[x+1]= lst2[x]
            names[x+1]=names[x]
            x -= 1
            
        lst2[x + 1] = key
        names[x + 1] = key2
    
    z = 0

    for y in lst2:
        output.append(names[z])
        output.append(y)

        z += 1
        
    return names
    
    
    
    
print(lst)
print()
print(sorting(names,lst2))
    