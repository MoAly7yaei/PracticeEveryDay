def run(year):

    if year % 4 == 0:
        print("Leap Year")
    else:
        print("Not a Leap year")
i = 0
while i < 1:
    year = int(input("Write the year: "))
    run(year)

