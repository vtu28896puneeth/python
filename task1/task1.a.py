principle=float(input("Enter the principle amount : "))
rate=float(input("Enter the rate of interest : "))
time=float(input("Enter the time in years : "))
compound_interest=principle*((1+rate/100)**time)-principle
print("The compound interest is : ",compound_interest)
