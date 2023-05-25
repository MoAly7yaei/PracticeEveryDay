word = ["HELLO", 'hello', 'WORLD', 'world']

x = list(filter(lambda i : i.isupper(), word))
y = list(filter(lambda i : i.islower(), word))


print(x)
print()
print(y)