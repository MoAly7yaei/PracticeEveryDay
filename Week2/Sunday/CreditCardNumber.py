string = input("Eter Credit Card number: ")
ccn = ""

ccn = string.replace(" -","")
ccn = ccn.replace(" ","")

print(ccn)