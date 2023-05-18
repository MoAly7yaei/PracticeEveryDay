"""
Expected Output

1 0 0 0
2 1 0 0
2 2 1 0
2 2 2 1

"""
lst = [[0,0,0,0] for i in range (4)] # Make Table of 4 Columns and 4 Rows of Zeros

for j in range(4):
    for k in range(4):
        
        if j == k: #If row = Column That will assign values in expected positions
            lst[j][k]= 1 
    
        if k < j: #If Column less then Row assign 2 in expected Positions
            lst[j][k]= 2
            
        print(lst[j][k] , end = " ")

    print()