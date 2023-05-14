from random import *

r = randint(1,100)

print("Insert Number between 0 - 100")

while True:
    user_input = int(input("Enter number: "))

    if user_input > 100 or user_input < 1:
        print("The number is out of range")
        
    else:
        
        if user_input > r:
            print("Go lower")
        
        elif user_input < r:
            print("Go Higher")
        
        elif user_input == r:
            print("Correct !, The answer is: ", r)
            break
                     
                 
