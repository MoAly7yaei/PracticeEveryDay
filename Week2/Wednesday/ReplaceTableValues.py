t = [[0]*3 for i in range(3)] #Make table of Zeros


#Replace Values
for j in range(3):
    for k in range(3):
        t[j][k]= j + 1
        print(t[j][k], end = " ")
    print()


