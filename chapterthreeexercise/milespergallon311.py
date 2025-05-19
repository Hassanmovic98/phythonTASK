gallon=float(input("enter the gallon used:"))
miles=float(input("enter miles driven:"))



if gallon > 0:
    mpg= miles / gallon
    print(f"miles per gallon is {mpg:.2f}")
else:
    print("gallon must be greater than 0")