word = input("Enter a username: ")
lst = list(word)
count = 0
unique = []
for i in lst:
    if lst.count(i) == 1:
        unique.append(i)
        
if len(unique) % 2 == 0:
    print("She is girl")

else:
    print("He is Boy")
