"""
This Program is been developed by Eng.Mohammed Al-Yahyai Instructed by Code Academy Instructors
Date: 8 May 2023
Version: 1.0
"""




def compare():

    x,y,z = 0,0,0
    x = input("Enter the First Number: ")
    y = input("Enter the Second Number: ")
    z = input("Enter the Third Number: ")
    numbers = [x,y,z]

    if numbers[0] == numbers[1]:

        if numbers[0] == numbers[2]:

            print("Numbers are Equal which is = ",numbers[0])

        else:

            print("The Maximum number is = ",max(numbers))
            print("The Minimum number is = ",min(numbers))
            
    else:

        print("The Maximum number is = ",max(numbers))
        print("The Minimum number is = ",min(numbers))

compare()