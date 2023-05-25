def febonacci_numbers(nums):
    x = 0
    y = 1
    for i in range(nums):
        x,y = y,x+y
        yield x
        
def cube(nums):
    for num in nums:
        yield num **3
        
print(sum(cube(febonacci_numbers(10))))

