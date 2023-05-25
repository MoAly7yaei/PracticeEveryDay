word = input("Enter names: ").split(" ")

a = list(map(lambda x : x.upper() , word))

print(a)