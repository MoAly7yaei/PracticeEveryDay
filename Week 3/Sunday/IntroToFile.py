"""
Exception Handling Example
"""

f = open("salery.txt" ,"w")

f.write("3522 Adam\n")
f.write("2232 Ahmed\n")
f.write("4232 Abdulla\n")
f.write("2234 Ali\n")
f.close()

try:
    f = open("saleryy.txt","r") #There is error
    for data in f:
        salery = data.split()
    f.close()
    
except IOError: #The excecution will handle 
    print("File not found")