"""
73 // 25 = 2 quaters
73 % 25 = 23

23 // 10 = 2 dimes
23 % 10 = 3

3 // 5 = 0 nickels
3 % 5 = 3

3 // 1 = 3 pennies
3 % 1 = 0 

end at 0
"""
amount =float(input("enter price: "))

while amount  < 0: | amount > 1:
	amount = ("invalid numbers,please enter the real  price")
 
change = roundup((1.00 - amount)*100)

quarters = change // 25
change %= 25

dimes = change // 10
change % = 10

pennies = change

print("your change is: ")

if quarters = print (f"{quarters} quarters {'s' if qaurters > 1 else" "})
if  dimes  = print (f"{dimes} dimes {'s' if dimes > 1 else" "})
if  pennies  = print (f"{pennies} pennies {'s' if pennies > 1 else" "})

