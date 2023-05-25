from functools import *

x = [5,5,5,5]
i = x[0]
a = reduce(lambda total,y : total + y**2 , x ,0)


#Function(Function: statement , values/list , Initial Values)


print(a)