temp = 0
ftemp = (temp * (9/5)) + 32
ctemp = (5/9)*(temp - 32)


user_io = int(input("Choose 1 to convert C to F or Choose 2 to convert F to C: "))

if user_io == 1:
    temp = float(input("Input Tempreture in Celius unit: "))
    print(ftemp)
elif user_io == 2:
    temp = float(input("Input Tempreture in Fahernhit unit: "))
    print(ctemp)