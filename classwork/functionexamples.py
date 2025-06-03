def get_square(number):
	return number ** 2

result = get_square (20)
print(result)



print(get_square(5))
print(get_square(15))
print(get_square(25), get_square(12))

def get_sum(number1, number2):
	return number1 + number2

x = int(input("enter number 1: "))
y = int(input("enter number2: "))
#print(get_sum(x, y))
#print(get_sum(2, 3))
get_sum(5,5)
"""
default arguement
positional has to come first
"""
def get_sum(x, y=3):
	return x + y
x = int(input("enter number 1: "))
y = int(input("enter number2: "))
print(get_sum(x, y))
print(get_sum("2,3 "))
get_sum("5,5")

"""
_ means something just has to be there
a throw away variable
"""
def display_name(age, name):
	for _ in range(age):
		print(name) 



display_name (name = "helen", age = 10)

print(2, "pathfinder")

def get_product(*numbers):
	print(numbers)
	product = 0
	for number in numbers:
		print(number)
		product *= product 

	return product 

print(get_product(3, 6, 5, 6, 7))

print(get_product( 4, 3, 7, 9, 10, 15, 23, 21, 12, 45))



"""
scope local and global

"""





