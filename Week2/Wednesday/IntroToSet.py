a = {1,2,3,4,5,6,7,8} #If it is empty it will classified as dicteionary
b = {2,4,6,8,10,12}
c = {}
d = {}
"""
The main Deferent between List and set that you cannot change the value and there is no index according to Jamal Al-Mahroqi
"""

a.remove(1) #It has to be specifid value

a.discard(3) #It will remove even when there is no similer value

a.update(b) #Similer to Union

b.add(14) #add values

c = b.copy() #Copy Values

d = b.difference_update(a) #Defference

#d.clear() Delete all the values

print(a)
print(c)
print(d)

#####
print()
#####

print(a|b) #Union
print(a&b) #Intersection
print(a^b) #Deferent things in two sets
print(a - b)#Deferent

#####
print()
#####

print(a.isdisjoint(b)) #Return true if there is no similer values in both sets

#set1.isupperset(set2) مجموعة شاملة
#set1.issubset(set2) مجموعة جزئية

"""
You're able to insert tuble into set but you're unable to insert list into set

There is a case to insert list in set is using update() function
"""


