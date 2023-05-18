# x = open("n.txt","w")
"""
r for read
w for write
close
"""
#######
#infile = open("t.txt","r")
#print(innfile)
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""
f = open("salery.txt" ,"w")

f.write("3522 Adam\n")
f.write("2232 Ahmed\n")
f.write("4232 Abdulla\n")
f.write("2234 Ali\n")
f.close()
f = open("salery.txt","r")
for data in f:
    salery = data.split()

f.close()