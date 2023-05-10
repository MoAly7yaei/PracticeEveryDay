sum = 0
mark = 0
i = 0
n = True

while(n == True):
    mark = float(input("Insert mark: "))
    sum = sum + mark
    n = (input("Another Student?: "))
    i += 1
print(sum / i)
