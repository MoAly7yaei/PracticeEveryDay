
word = input("Enter a word: ")
c = int(input("Enter a number: "))

def split(word,c):
    x = int(len(word) / c)
    reasult = []
    if len(word) % c == 0:
        for i in range(0,len(word),x):
            
            reasult.append(word[i:i + x])
            i += 1


    else:
        reasult = 'Invalid Input'
    return reasult

print(split(word,c))

