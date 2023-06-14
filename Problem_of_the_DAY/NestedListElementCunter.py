lst = [1,[2,3,4,5,[6,7,8,[9,10,[11,12,[13]]]]]]
def read_array(lst):
    counter = 0
    for i in lst:
        
        if type(i) == list:
            for j in i:
                if type(j) == list:
                    counter = counter + read_array(j)
                
                else:
                    counter = counter + 1

        else:
            counter += 1
    return counter
print(read_array(lst))
