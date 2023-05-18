values = open("values.txt", "r")


for i in values:
    x=i.split()
    
    reasult = int(x[0]) * int(x[1])
    print(reasult)
