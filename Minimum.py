"""find the minimum of three number"""

number1 = int(input('Enter first integer'))
number2 = int(input('Enter second integer'))
number3= int(input('Enter thirdinteger'))

minimum = number1

if number2 < minimum:
	minimum = number2

if number3 < minimum:
	minimum = number
print('Minimum value is', minimum)