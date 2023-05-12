from main import scale_finder
i = 5

while i != 0:
    n = int(input("You have to select the root note of the scale using numbers (Read the Readme.txt file for more details): "))
    scale_name = input("You have to select the name of the scale mentioned in Readme.txt: ")
    print(scale_finder(n, scale_name), end = "   ")
    print()
    i -= 1