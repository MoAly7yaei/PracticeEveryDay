text = "Mohammed"
n = len(text) 
p = int((n - 1) / 2)

if n % 2 == 0:
    print(text[p] + text[p+1])
else:
    print(text[p])
