def even(nums):
    for i in nums:
        if i % 2 == 0:
            yield i
        
        
nums = [j for j in range(1,16)]
x = even(nums)
 
for i in x:
    print(i)