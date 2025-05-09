number=input("Enter five digit numbers: ")

if len(number) == 5 and number.isdigit():

	print('   '.join(number))
else:
	print("invalid number.kindly enter five digit numbers.")




