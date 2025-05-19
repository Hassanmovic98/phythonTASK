

number = 0
userinput = int(input("Enter input :"))

number = userinput
value = 0
divider = 0
counter = 0
sum = 0

while(number > 0):
	divider = number % 10
	number = number // 10

	value = divider * (2 ** counter)
	counter += 1

	sum += value



print(sum)





 





