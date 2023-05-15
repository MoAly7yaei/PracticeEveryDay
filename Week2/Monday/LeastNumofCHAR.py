names = ['Mohammed','Ahmed','Abdullah','Moeen','Ali','Issa']

n = int(input("Least numberof Charecters: "))

for i in range(len(names)):
    l = len(names[i])
    if n <= l:
        print(names[i])
    else:
        pass
