n = int(input("Type a number: "))
i = 1
while i <= (n + 1/2):
    c = n / i
    if n % i == 0:
        print(int(c))
    i += 1