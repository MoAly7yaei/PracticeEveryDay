"""
Expected Output

1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1

"""
lst = [[0,0,0,0] for i in range (4)] # Make Table of 4 Columns and 4 Rows of Zeros
for j in range(4):
    for k in range(4):
        
        if j == k: #If row = Column That will assign values in expected positions
            lst[j][k]= 1
            lst[j][k-2]= 1


    
for x in range(4):
    for y in range(4):
        print(lst[x][y] , end = " ")
    
    print()