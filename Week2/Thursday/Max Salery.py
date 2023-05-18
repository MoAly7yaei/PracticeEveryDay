"""
Print Highest Salery

"""


f = open("salery.txt" ,"w")

f.write("3522 Adam\n")
f.write("2232 Ahmed\n")
f.write("4232 Abdulla\n")
f.write("2234 Ali\n")
f.close()
f = open("salery.txt","r")

salery = []
v = []
i = 0
name = []
max_name = ""
for data in f:
    
    salery = data.split()
    v = v + [int(salery[0])]
    name = salery[1]
    i += 1
    
max_value = max(v)

print(" ",max_value)
f.close()