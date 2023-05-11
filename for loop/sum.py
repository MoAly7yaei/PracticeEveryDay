"""
For loop Program instructed by Code Academy Instructors
Developed by Mohammed Al-Yahyai
"""

total = 0
value = 0
#count = 0

c = int(input("How many Values you went to insert?: "))

value = int(input("Enter Value: "))

total = total + value

for i in range(c-1):
    
        if value < 0:
            break
        else:
            value = int(input("Enter Value: "))

        total = total + value
        

if total > 0:
    
    print("Total is: ",total)
    print("Inserted value is: ",(c))
    print("average is: ",(total/(c)))
else:
    
    print("No calculation occur")

        
        