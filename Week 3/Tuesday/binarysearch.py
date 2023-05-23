x = [1,2,3]
n,mid,minimum,maximum = 0,0,0,0

def binarysearch(x,target):
    

    minimum = x.index(min(x))
    maximum = x.index(max(x))
    
    for i in x:
        n = (minimum + maximum)
        mid = n // 2
        if target == x[mid]:
            return mid
        elif target > x[mid]:
            minimum = mid + 1
        elif target < x[mid]:
            maximum = mid - 1
    
        
    
    return "not found"

print(binarysearch([1,2,3,4,5,6,7,8],8))
    
    