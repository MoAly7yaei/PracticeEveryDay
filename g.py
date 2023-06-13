lst = [1,[2,[3,[4]]]]
counter = 0
def read_array(lst):
    global counter
    for i in lst:
        
        if type(i) == list:
            for j in i:
                if type(j) == list:
                    counter = counter + len(i)
                
                else:
                    counter = counter + 1

        else:
            counter += 1
    return counter
print(read_array(lst))
