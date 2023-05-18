"""
2D Lists
Tables

    ***Important notation***
    
    First Loop ---->	Row
    Second Loop --->	Column
        

"""

"""
[Row][Column] ---> Important to locating elements

"""
lst = [[1,2,3],
       [4,5,6]]

#To print one row
"""
for i in lst[0]:
    print(i , end=" ")
"""

# To print Two Row
"""
for i in lst:
    print(i[0] , end=" ")
"""

#To print all List
"""
for i in range(2): #No of Rows
    for j in range(3): #No of Column
        print(lst[i][j] , end="")
    print() #Print New Line
"""

#Compute total Column values
"""
total = 0
for i in range(2): # Range 2 indecates No of Rows
    total = total + lst[i][0] #Variable i is indecate Change in rows to Adding the same column value
print(total)
"""

#Compute total row Values
"""
total = 0
for i in range(3): #Range 3 Indecates No of Columns
    total = total + lst[0][i] #Variable i is indecate Change in rows to Adding the same column value
print(total)
"""

#Create Table
"""
tbl = [[0]*3 for i in range(3)] #Creating 3 Rows and for loop will create 3 Column
print(tbl)
"""