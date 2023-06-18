word = input("Enter a username: ")
count = 0

for i in word:
    for j in word:
        if i == j:
            break
        else:
            count += 1

if count % 2 == 0:
    print("She is a girl")
else:
    print("He is a boy")