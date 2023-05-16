i = 1
j = 0
k = 0

#while k != 8:
for k in range(8):
    print("    "*int(15 - k), end = "")
    print(int(i), end="   ")
    for j in range(k):
        i = i*2
        print(int(i), end="   ")

        j+=1
    while j != 0:
        i = i/2
        print(int(i), end="   ")

        j-=1
    print()
    k+=1