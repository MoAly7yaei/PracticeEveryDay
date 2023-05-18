"""
Creating Table Using User Inputs
"""

c = int(input("No of Columns: ")) #Going to be used in Range of for Loop
r = int(input("No of Rows: ")) #Going to be used in Range of for Loop

# Concept is [[Expression to input with for loop to make row]for loop to make columns]
l = [[int(input("Enter The Data: ")) for j in range(r)] for i in range(c)]



for x in range(r):
    for y in range(c):
        print(l[x][y] , end = " ")
    
    print()