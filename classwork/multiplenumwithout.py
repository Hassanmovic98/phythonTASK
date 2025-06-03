def multiple(number1,number2):
	result =0
	for number in range (0, number1):
		result= result + number2
	return result
print(multiple(2,8)) 
print(multiple(3,3))
print(multiple(4,9))
print(multiple(5,100))
print(multiple(5000,5000))