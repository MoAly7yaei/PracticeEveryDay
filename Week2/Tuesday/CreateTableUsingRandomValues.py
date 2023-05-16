import random

# Table is List and List
COUNTRIES = 8 #Rows
MEDALS = 3 #Columns
count = []

for i in range(COUNTRIES):
    count = []
    for j in range(MEDALS):
        value = random.randint(1,2)
        count.append(value)
    print(count)
        