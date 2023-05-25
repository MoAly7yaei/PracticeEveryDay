"""
Filter will test all values in the list
"""
x = [-4,8,-2,7,4,-2,-3]

nx = list(filter(lambda y: y>=0 , x))

print(nx)