
year = 10
add_year = 4
cost = 10000
total_cost = 0
vat = 0.05
i = 0
sub_year = 0
total_year = 10 + 4

while i != total_year:
    total_cost = cost + total_cost
    total_cost = total_cost + (total_cost*vat)
    i += 1
i = 0
while i != 10:
    sub_year = cost + sub_year
    sub_year = sub_year + (sub_year*vat)
    i += 1

print("Total = %.3f"%total_cost)
print("4 Years after the 10 Years = %.3f"%(total_cost - sub_year))