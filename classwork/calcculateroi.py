investment =int(input("enter amount of investment"))
year=int(input("enter number of years"))
interest =int(input("enter interest rate"))
intrest_rate =interest/100



for count in range (1,year+1):
	roi=investment * intrest_rate 
	investment = roi + investment
	print(f"investment after {count}years is {investment:.2f}")