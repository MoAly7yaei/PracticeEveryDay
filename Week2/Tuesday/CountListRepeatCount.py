x = [1,2,3,4,5,6]
counter = [0,0,0,0,0,0]
#n = int(input("How many tried you went to insert?: "))
resault = []
ins = int()
j = 0
def main():
    insert()
    print(x)
    print(counter)
        

def insert():
    reasult = [1,3,2,4,3,3,6,6] # Inputs
    for i in reasult:
        counter[i - 1] = counter[i - 1] + 1 
    
    return counter
    

main()      
            
